import logging 
import os

from crewai.tools import tool
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from src.agents_src.config.agent_settings import agentsettings

settings = agentsettings()

# Get a logger for this module
logger = logging.getLogger(__name__)

logger.info("downloading embedding model")
embeddings = HuggingFaceEmbeddings()

@tool
def rag_query_tool(user_query:str)->dict:

    """
    Answers a query by retrieving relevant documents and generating a response.
    Returns both the generated answer and the source file names from which the information was retrieved.

    Args:
        query (str): The input query string to be processed.

    Returns:
        dict: A dictionary with the following keys:
            - 'answer': The generated answer string.
            - 'source_files': List of source file names used for retrieval.

    Notes:
        - Requires properly configured AgentSettings and access to the vector store.
        - The function loads the embedding model and LLM each time it is called.
    """

    vector_db_path = settings.VECTOR_STORE_DIR
    model_name = settings.GROQ_MODEL_NAME
    model_temperature = settings.MODEL_TEMPERATURE
    groq_api_key = settings.GROQ_API_KEY

    vector_store = Chroma(embedding_function = embeddings,persist_directory = vector_db_path)
    logger.info("vector_embeddings loaded")
    llm = ChatGroq(api_key = groq_api_key,model = model_name,temperature = model_temperature)
    logger.info("llm created")
    chain = RetrievalQA.from_llm(
        llm =llm,
        # chain_type = "stuff",
        retriever = vector_store.as_retriever(search_type = "mmr",search_kwargs={'k':3}),
        verbose = True,
        return_source_documents = True
    )
    logger.info("Chain created")
    response = chain.invoke({'query':user_query})
    # source_file_names = {m.get("filename") for m in getattr(response,"metadata",{})}
    source_file_names = {os.path.basename(doc.metadata.get("source")) for doc in response["source_documents"]}
    # os.path.basename give only the file name

    return {
        "answer":response["result"],
        "source_files":list(source_file_names)
    }

# ans = rag_query_tool("Explain diversity and classification")
# print(ans)
# print(ans["answer"])
# print(ans["source_files"])

