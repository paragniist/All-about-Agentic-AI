from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CCoder():
    """
    Plant researcher crew
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def research(self) ->Agent:
        return Agent(
            config = self.agents_config['researcher'],verbose = True
        )

    @agent
    def analyst(self) ->Agent:
        return Agent(
            config = self.agents_config['analyst'],verbose=True
        )

    @task
    def plant_growth_task(self) -> Task:
        return Task(
            config = self.tasks_config('plant_growth_task')
        )
    
    @task
    def reporting_task(self) -> Task:
        return Task(
            config = self.tasks_config('reporting_task')
        )

    @crew
    def crew(self)->Crew:
        return Crew(
           agents = self.agents,
           tasks = self.tasks,
           process = Process.sequential,
           verbose = True
    )