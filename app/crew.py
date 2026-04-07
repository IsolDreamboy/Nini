from app.agents.Nini import Nini
from app.NiniTasks.NiniTaskTriage import NiniTaskTriage
from crewai import Crew

class NiniCrew:
    def crew(self)-> Crew:
        return Crew(
            agents=[Nini],
            tasks=[NiniTaskTriage],
            verbose= True
        )
