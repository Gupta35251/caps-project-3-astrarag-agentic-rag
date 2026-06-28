import logging
from src.agents_src.crew import qa_crew

logger = logging.getLogger(__name__)

def get_ans(chat_history:str)->dict:
    logger.info(f"Received Chat History : {chat_history}")
    last_user_message = chat_history[-1]
    user_query = last_user_message["content"]
    logger.info(f"Extracted user query : {user_query}")
    # Remove the last user message from the chat history
    history_without_last = chat_history[:-1]
    input_data = {
        "user_query" : user_query,
        "chat_history" : history_without_last
    }

    logger.debug("input data for qa_crew: {input_data}")
    response = qa_crew.kickoff(input_data)
    response_dict = response.to_dict()
    logger.info(f"Result from qa_crew : {response_dict}")
    return response_dict

