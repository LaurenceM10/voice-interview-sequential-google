import asyncio  
import os  
from google.adk.runners import Runner  
from google.adk.agents.run_config import RunConfig  
from google.adk.agents.live_request_queue import LiveRequestQueue  
from google.genai import types  
from dotenv import load_dotenv  
  
load_dotenv()  
  
async def run_voice_interview():  
    from src.interview_agents.system.agent import root_agent  
      
    runner = Runner(agent=root_agent)  
      
    # Configuración específica para voice mode  
    run_config = RunConfig(  
        response_modalities=['AUDIO'],  
        input_audio_transcription=types.AudioTranscriptionConfig(),  
        output_audio_transcription=types.AudioTranscriptionConfig(),  
        enable_affective_dialog=True  
    )  
      
    live_request_queue = LiveRequestQueue()  
      
    print("🎤 Sistema de Entrevistas Secuencial iniciado...")  
    print("📋 Flujo: Entrevistador → Estratega → Entrevistador → ...")  
      
    try:  
        async for event in runner.run_live(  
            user_id="interviewer",  
            session_id="sequential_interview",  
            live_request_queue=live_request_queue,  
            run_config=run_config  
        ):  
            if hasattr(event, 'content') and event.content:  
                print(f"💬 {event.agent_name}: {event.content}")  
                  
    except KeyboardInterrupt:  
        print("\n🛑 Entrevista terminada")  
  
if __name__ == "__main__":  
    asyncio.run(run_voice_interview())