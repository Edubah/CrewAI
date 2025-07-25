#Importando as bibliotecas necessárias
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

#Chamar os modelos do Gemini
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

#Criação de um agente de pesquisa sénior com memória e modo detalhado

#Agente programado para pesquisar notícias
news_researcher=Agent( 
                      
    role="Senio Researcher",
    goal='Unccover ground breaking technologiies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and shar knowledge that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True,
    
)

#Agente escritor com ferramentas customizadas responsável por escrever artigos
news_writer=Agent(
    role='Writer',
    goal="Narrate compelling tech strories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate bringin new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False,
)


