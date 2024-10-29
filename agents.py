from crewai import Agent
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define Agents
industry_researcher = Agent(
    role="Industry Research Specialist",
    goal="Research and analyze industry trends and company details for {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in conducting comprehensive industry analysis, understanding "
        "business landscapes and identifying strategic focus areas across "
        "different sectors."
    ),
    tools=[],
    llm=llm,
    allow_delegation=True
)

usecase_generator = Agent(
    role="Market Standards & Use Case Generator",
    goal="Generate AI/GenAI use cases and analyze market standards for {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Specialized in identifying AI/ML opportunities and analyzing industry "
        "standards to propose relevant use cases that improve processes and "
        "enhance customer satisfaction."
    ),
    tools=[],
    llm=llm,
    allow_delegation=True
)

resource_collector = Agent(
    role="Resource Asset Collector",
    goal="Collect and organize AI/ML resources and datasets for {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in finding and organizing relevant AI/ML datasets and resources "
        "from platforms like Kaggle, HuggingFace, and GitHub."
    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)

final_proposal_writer = Agent(
    role="Final Proposal Writer",
    goal="Create comprehensive final proposal with top use cases and references",
    verbose=True,
    memory=True,
    backstory=(
        "Specialized in creating detailed final proposals that highlight top "
        "AI/ML use cases with proper references and clickable resource links."
    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)