from pprint import pprint  #prettyprint -> Prints complex data (lists, dictionaries, JSON) in a well-formatted, readable way.

from src.agents_src.crew import qa_crew

input_data = {
    "user_query" : "What is DIversity and Classification?",
    "chat_history" : "{}"
}

result = qa_crew.kickoff(input_data)
result_dict = result.to_dict()
pprint(result_dict)

