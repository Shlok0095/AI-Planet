from crewai import Task
from tools import tool
from agents import industry_researcher, usecase_generator, resource_collector, final_proposal_writer

industry_analysis_task = Task(
    description=(
        "Conduct a deep dive analysis of {company}'s industry and market position."
    ),
    expected_output='A detailed 5-section report covering industry analysis, market positioning, and tech adoption patterns.',
    tools=[tool],
    agent=industry_researcher
)

usecase_generation_task = Task(
    description=(
        "Generate comprehensive AI/GenAI use cases based on the industry analysis."
    ),
    expected_output='A prioritized list of 10 AI/GenAI use cases with ROI analysis and implementation examples.',
    tools=[tool],
    agent=usecase_generator
)



# Resource Collection Task
resource_collection_task = Task(
    description=(
        "Collect the use cases generated and search for relevant datasets on Kaggle, HuggingFace, and GitHub.\n"
        "Save the resource links fetched in a text or markdown file.\n"
        "[OPTIONAL: BONUS] If applicable, propose GenAI solutions like document search, automated report generation, "
        "and AI-powered chat systems for internal or customer-facing purposes."
    ),
    expected_output="A markdown file with links to relevant datasets and optional GenAI solution proposals.",
    tools=[tool],
    agent=resource_collector,
    output_file="ai_resources.md"
)


final_proposal_task = Task(
    description=(
        "Create a compelling final proposal document."
    ),
    expected_output='A comprehensive final proposal document in markdown format with all sections and clickable references.',
    tools=[tool],
    agent=final_proposal_writer,
    async_execution=False,
    output_file='final_proposal.md'
)  