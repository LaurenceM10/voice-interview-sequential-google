from google.adk.agents import SequentialAgent  
from ..interviewer.agent import root_agent as interviewer_agent  
from ..strategist.agent import root_agent as strategist_agent  
  
root_agent = SequentialAgent(  
    name="VoiceInterviewSystem",  
    description="Sistema completo de entrevistas por voz con análisis estratégico secuencial",  
    sub_agents=[interviewer_agent, strategist_agent]  
)