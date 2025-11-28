from urllib import response
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.agents import create_agent
from dotenv import load_dotenv

# from src.utils.prompt import EMAIL_TEMPLATE_PROMPT , HTML_EMAIL_TEMPLATE_PROMPT
from src.utils.prompt import PromptList
from src.state.states import DataModel
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
# from langchain.agents import AgentExecutor
from src.helper.helper_function import image_search
load_dotenv()


tools = [image_search]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.7)
# llm = ChatOpenAI(model = "o4-mini")
llm_structure = llm.with_structured_output(DataModel)


# agent = create_react_agent(model = llm, tools = tools, prompt = PromptList.EMAIL_TEMPLATE_PROMPT , response_format=DataModel)
agent = create_react_agent(model = llm, tools = tools, prompt = PromptList.HTML_EMAIL_TEMPLATE_PROMPT , debug = True)
