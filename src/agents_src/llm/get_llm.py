from crewai import LLM
from src.agents_src.llm.llm_configuration import LLM_CONFIGURATION

def get_llm_for_agent(agent_name):
    model = LLM_CONFIGURATION.get(agent_name,{}).get("model","groq/llama-3.3-70b-versatile")
    temperature = LLM_CONFIGURATION.get(agent_name,{}).get("temperature",0.0)
    llm = LLM(
        model = model,
        temperature = temperature
    )
    return llm

