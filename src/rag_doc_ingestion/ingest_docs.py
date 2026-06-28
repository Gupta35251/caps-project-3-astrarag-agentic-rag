import logging  # Builtin library in python no need to install

from langchain_community.document_loaders import DirectoryLoader,UnstructuredFileLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from src.rag_doc_ingestion.config.doc_ingestion_settings import DocIngestionSettings

# Set up logging configuration 
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"    
)

# Get a logger for this module
logger = logging.getLogger(__name__)

# Load settings from environment variables
settings = DocIngestionSettings()

# Loading the embeddings model
embeddings = HuggingFaceEmbeddings()

doc_dir = settings.DOCUMENTS_DIR 
vector_db_path = settings.VECTOR_STORE_DIR

logger.info("Embedding Model Loaded")

def build_vector_db():
    logger.info("Loading the directory")
    try:
        loader = DirectoryLoader(doc_dir,glob = "**/*.pdf",loader_cls = UnstructuredFileLoader)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(
            chunk_size = 2000,
            chunk_overlap = 500
        )
        chunks = text_splitter.split_documents(documents)
        vector_db = Chroma.from_documents(embedding = embeddings,documents = chunks,persist_directory = vector_db_path)
        logger.info("vector_db created for the data")
        return 0
    except Exception as e:
        logger.error("Error during vector store build : {e}")
        return 1
    
if __name__ == "__main__":
    build_vector_db()