from crewai import Task

#Tarefa de pesquisa de notícias
reseach_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should cleary articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=[tool_search],
    agent=researcher,
)