from crewai import Crew, Process
from app.agents.Nini import Nini
from app.agents.MimicAgent import MimicAgent
from app.agents.PubAgent import PubAgent
from app.agents.Judge import Juiz
from app.NiniTasks.NiniTaskTriage import NiniTaskTriage
from app.NiniTasks.MimicTask import MimicAgentTask
from app.NiniTasks.PubTask import PubMedTask
from app.NiniTasks.JudgeTask import JudgeTask


class NiniCrew:
    def crew(self)-> Crew:
        return Crew(
            agents=[Nini,MimicAgent,PubAgent,Juiz],
            tasks=[NiniTaskTriage,MimicAgentTask,PubMedTask,JudgeTask],
            verbose= True,
            process = Process.sequential
        )
