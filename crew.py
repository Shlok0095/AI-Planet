from crewai import Crew, Process
from tasks import (industry_analysis_task,
                   usecase_generation_task,
                   resource_collection_task,
                   final_proposal_task)

from agents import (industry_researcher,
                    usecase_generator,
                    resource_collector,
                    final_proposal_writer)



crew = Crew(
    agents = [industry_researcher, usecase_generator, resource_collector, final_proposal_writer],
    tasks = [industry_analysis_task, usecase_generation_task, resource_collection_task, final_proposal_task],


    process = Process.sequential,

)


result = crew.kickoff(inputs={'topic': 'AI in Automotives', 'company':'Tesla'})

print(result)