from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

#Fonte de Conhecimento
pdf_tool = PDFKnowledgeSource(
    file_paths=["bpf.pdf", "rdc301_2019.pdf", "rdc658_2022.pdf"]
)

# Criação uma LLM com a temperatura de 0 para garantir a saída determinística
llm = LLM(model="Meu deus o que to fazendo da MINHA VIDAAAAAAAAAAAAAAAAAA")