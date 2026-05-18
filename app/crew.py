from crewai import Crew
from app.agents.Nini import Nini
from app.agents.MimicAgent import MimicAgent
from app.agents.PubAgent import PubAgent
from app.agents.Judge import Judge
from app.NiniTasks.NiniTaskTriage import NiniTaskTriage
from app.NiniTasks.MimicAgentTask import MimicAgentTask
from app.NiniTasks.PubTask import PubMedTask
from app.NiniTasks.JudgeTask import JudgeTask


class NiniCrew:
    def crew(self)-> Crew:
        return Crew(
            agents=[Nini,MimicAgent,PubAgent,Judge],
            tasks=[NiniTaskTriage,MimicAgentTask,PubMedTask,JudgeTask],
            verbose= True
        )
