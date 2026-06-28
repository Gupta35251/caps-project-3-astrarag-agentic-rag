from crewai import Crew
from src.agents_src.agent.question_answer_agent import agent
from src.agents_src.tasks.question_answer_task import qa_task 

qa_crew = Crew(
    agents = [agent],
    tasks = [qa_task],
    verbose = True
)