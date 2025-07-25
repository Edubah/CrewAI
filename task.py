from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

#Tarefa de pesquisa de notícias
reseach_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should cleary articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=[tool],
    agent=news_researcher,
)

#Tarefa de escrita de notícias com a configuração do modelo de linguagem
write_task = Task(
    description=(
        "Compose an insighful article on {topic}."
        "Focus on the latest trend and how it's impacting the industry."
        "This article should be easy to understand, engagin, and positive."
    ),
    expected_output='A 4 paragraphs article on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent=news_researcher,
    async_execution=False,
    output_file='new-blog-post.md' #Exemplo de customização de saída
)

