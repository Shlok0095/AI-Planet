#serper tool (https://serper.dev/)
from dotenv import load_dotenv
load_dotenv()
import os


from crewai_tools import SerperDevTool

#internet searching capability tools

tool = SerperDevTool()