from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from utils.prompt import PromptList
from response_structure.response_structure import DataModel

from langgraph.prebuilt import create_react_agent
from helper.helper_function import image_search

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env.local"))


tools = [image_search]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 1)
# llm = ChatOpenAI(model = "o4-mini")
llm_structure = llm.with_structured_output(DataModel)


agent = create_react_agent(model = llm, tools = tools, prompt = PromptList.EMAIL_TEMPLATE_PROMPT.value , response_format=DataModel)