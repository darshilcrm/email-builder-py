from urllib import response
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.agents import create_agent
from dotenv import load_dotenv

from src.utils.prompt import EMAIL_TEMPLATE_PROMPT 
from src.state.states import DataModel
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
# from langchain.agents import AgentExecutor
from src.helper.helper_function import image_search
load_dotenv()


tools = [image_search]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 1)
# llm = ChatOpenAI(model = "o4-mini" , temperature = 1)
llm_structure = llm.with_structured_output(DataModel)

# agent = create_react_agent(
#     model=llm,
#     prompt=EMAIL_TEMPLATE_PROMPT,
#     debug=True ,
#     tools=[image_search],
#     response_format=DataModel
#     )

agent = create_react_agent(model = llm, tools = tools, prompt = EMAIL_TEMPLATE_PROMPT , response_format=DataModel , debug = True)
# agent_executor = AgentExecutor(agent=agent, tools=tools)
# (1) 2 colomn layout
# - column/2-50-image-text-button (Means both columns have image, text and button)
# - column/1-50-image/1-50-text-button (Means first column has image, second column has text and button)
# - column/1-50-text-button/1-50-image (Means first column has text and button, second column has image)
# - column/1-50-image/1-50-text   (Means first column has image, second column has text)
# - column/1-50-text/1-50-image (Means first column has text, second column has image)
# - column/2-50-image (Means both columns have image)
# - column/2-50-button (Means both columns have button)

# (2) 3 Column layout
# - column/3-33-image-text-button (Means all three columns have image, text and button)
# - column/3-33-image-text (Means all three columns have image and text)
# - column/3-33-image (Means all three columns have image)
# - column/1-33-image/2-33-text (First column has image, second and third columns have text)
# - column/2-33-text/1-33-image (First and second columns have text, third column has image)
# - column/3-33-text (Means all three columns have text)
# - column/3-33-button  (Means all three columns have button)

# (3) 4 column layout:
# - column/4-25-image-text-button (Means all four columns have image, text and button)
# - column/4-25-image-text (Means all four columns have image and text) 
# - column/4-25-image (Means all four columns have image)
# - column/1-25-image/1-25-text/1-25-image/1-25-text (Means first column has image, second column has text, third column has image, fourth column has text)
# - column/1-25-text/1-25-image/1-25-text/1-25-image (Means first column has text, second column has image, third column has text, fourth column has image)
# - column/1-25-image/3-25-text (Means first column has image, rest three columns have text)
# - column/4-25-text (Means all four columns have text)
# - column/4-25-button (Means all four columns have button)