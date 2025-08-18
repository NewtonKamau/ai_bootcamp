# Install dependencies if not done
# pip install langchain langchain-openai crewai ipython

from langchain_openai import ChatOpenAI
from crewai import Agent, Process, Crew, Task
from IPython.display import display, Markdown
import os

# Load LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Define job info (you must supply these)
interviewer = "HR Specialist"
company = "White Tigers Club"
job_position = "Senior Consultant/Instructor"
job_description = "Responsible for coaching, mentoring, and overseeing sports programs at the county and national level."

# Create interviewer agent
interviewer_agent = Agent(
    role=f"You are an {interviewer} employed at {company}, hiring for the position {job_position}.",
    goal=f"You help the user prepare for the {job_position} role with the following job description: {job_description}",
    backstory="""
    Extensive experience in sports program management, advisory services, and leadership in national federations.
    Skilled in identifying local talent, promoting county sports programs, and coordinating improvement of facilities.
    """,
    llm=llm
)

# Define the task
interview_prep_task = Task(
    description=f"Interview the user for the job {job_position}. Job description: {job_description}",
    expected_output=f"Ask only one question to the user that is relevant for the job {job_position}.",
    agent=interviewer_agent,
    human_input=True
)

# Build crew
crew = Crew(
    agents=[interviewer_agent],
    tasks=[interview_prep_task],
    verbose=True,
    process=Process.sequential
)

# Run
result = crew.kickoff()
display(Markdown(f"### Result\n{result}"))
if __name__ == "__main__":
    crew.kickoff()
