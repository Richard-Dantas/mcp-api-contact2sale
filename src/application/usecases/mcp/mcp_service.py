import asyncio
import httpx
import json
import os
from fastmcp import Client
from dotenv import load_dotenv

load_dotenv()

class MCPService:
    def __init__(self):
        self.client = Client("/app/src/infrastructure/mcp/server.py")
        self.ollama_api_url = os.getenv("OLLAMA_API_URL", "http://ollama:11434/api/generate")
        self.ollama_model_name = os.getenv("OLLAMA_MODEL_NAME", "llama3")

    async def call_agent(self, user_prompt: str) -> str:
        """
        Envia o prompt para o Ollama decidir qual ferramenta MCP usar
        e retorna o resultado da execução real no servidor MCP.
        """
        async with self.client:
            tools = await self.client.list_tools()

            full_prompt = self._build_prompt(user_prompt, tools)

            payload = {
                "model": self.ollama_model_name,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "top_p": 0.9
                }
            }

            async with httpx.AsyncClient() as client_http:
                response = await client_http.post(
                    self.ollama_api_url,
                    json=payload,
                    timeout=120.0
                )
                response.raise_for_status()
                output = response.json()

            model_reply = output.get("response", "").strip()
            try:
                action = json.loads(model_reply)
            except json.JSONDecodeError:
                return f"Resposta inválida do modelo: {model_reply}"

            tool_name = action.get("tool")
            parameters = action.get("parameters", {})

            if not tool_name:
                return "Nenhuma ferramenta foi selecionada pelo modelo."
            
            try:
                raw_response = await self.client.call_tool(tool_name, parameters)
            except Exception as e:
                return f"Erro ao executar a ferramenta '{tool_name}': {e}"

            beautify_prompt = f"""
                Você é um assistente virtual de veículos que costuma retornar para o usuários os veículos que ele consultou.

                Recebeu os seguintes veículos encontrados que normalmente vem com os atributos brand, model, year, engine(que é o motor) e price:

                {raw_response}

                Lembrando que você fala português

                Sua tarefa:
                - Apresente esses veículos de forma clara e amigável para o usuário.
                - Seja breve e objetivo.
                - NÃO invente marcas, preços ou características.
                - Se houver mais de um veículo, liste todos de maneira agradável, citando qual é a marca, o model etc.

                Monte a resposta como se estivesse conversando com o usuário
            """
            final_response = await self._ask_ollama(beautify_prompt)
            return final_response

    def _build_prompt(self, user_prompt: str, tools: list) -> str:
        """
        Monta o prompt explicando ao modelo que ele deve escolher o tool e retornar JSON.
        """
        tools_list = "\n".join(f"- {tool.name}: {tool.description}" for tool in tools)

        return f"""
Você é um assistente inteligente. As ferramentas disponíveis são:

{tools_list}

Ao receber uma pergunta do usuário, você deve:
- Escolher a ferramenta mais adequada.
- Extrair e preencher os parâmetros necessários para a ferramenta.
- Responder apenas com um JSON no seguinte formato:

{{
  "tool": "<nome_da_ferramenta>",
  "parameters": {{
    "param1": "valor1",
    "param2": "valor2"
  }}
}}

Exemplo:

Pergunta do usuário: "Me mostre dois veículos têm motor 3.0 com preço acima de 200000"
Resposta esperada:
{{
  "tool": "get_vehicle_by_attributes",
  "parameters": {{
    "engine": "3.0",
    "price": {{"$gt": 200000}},
    "limit": 2
  }}
}}

Agora, responda à pergunta do usuário lembrando de retornar apenas e exclusivamente o JSON e que o valor máximo e padrão para limit é 10:

Pergunta do usuário: "{user_prompt}"
"""

    async def _ask_ollama(self, prompt: str) -> str:
        """
        Função para enviar prompts ao Ollama e receber resposta.
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": self.ollama_model_name,
            "prompt": prompt,
            "stream": False
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.ollama_api_url,
                headers=headers,
                json=payload,
                timeout=200.0
            )
            response.raise_for_status()
            try:
                data = response.json()
                return data.get("response", "").strip()
            except Exception:
                return (await response.aread()).decode().strip()
        