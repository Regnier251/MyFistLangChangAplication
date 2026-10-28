from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model="qwen2.5:1.5b",
    base_url="http://10.1.3.13:11434",
    temperature=0.7,
)

messages = [
    SystemMessage(content="Eres un asistente útil."),
    HumanMessage(content="Hola desde otra máquina de la red, ¿funcionas correctamente?"),
]

response = llm.invoke(messages)
print(response.content)