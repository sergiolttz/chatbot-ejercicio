from langgraph.prebuilt import create_react_agent

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langgraph.graph import MessagesState, add_messages
from langgraph.managed import IsLastStep
from typing import Annotated, TypedDict, Optional
from langgraph.checkpoint.memory import MemorySaver

from agentes.tools import tavily_search_tool
from core.config import model

tools = [tavily_search_tool]

#graph basico
graph = create_react_agent(model, tools=tools)


#graph2

system_propmt="""
Eres un agente experto en deportes, te llamas Agente Deportes y tus funciones son:
    - Buscar informacion sobre deportes: Utiliza la API Tavily para buscar información sobre deportes.
    - Generar un resumen de deportes: Utiliza la API Tavily para generar un resumen de deportes.

    Tus respuestas deben ser cortas y concisas y deben contener solo información relevante. No incluyas información que no esté relacionada con el deporte.
    """

chat_template_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_propmt),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

graph2 = create_react_agent(
    model,
    tools=tools,
    prompt=chat_template_prompt
)

# Agente 3

system_propmt3="""
Eres un agente experto en Cocina, te llamas Coci y tus funciones son:
    - Buscar recetas: Utiliza la API Tavily para buscar recetas.
    - Generar un resumen de cocina: Utiliza la informacion obtenida de la API Tavily para generar un resumen de cocina
    - La respuesta debe estár en formato Markdown

    Tus respuestas deben ser cortas y concisas y deben contener solo información relevante. No incluyas información que no esté relacionada con el tema.
    """

chat_template_prompt_3 = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_propmt3),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# State
#class CustomState(MessagesState):
#   remaining_steps: IsLastStep

class CustomState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    is_last_step: IsLastStep
    remaining_steps: Optional[int] = None

graph3 = create_react_agent(
    model,
    tools=tools,
    prompt=chat_template_prompt_3,
    state_schema=CustomState,
    checkpointer=MemorySaver()
)


