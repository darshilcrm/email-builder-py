from fastapi import FastAPI , Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.utils.prompt import *
from src.llm.llm import llm , agent , llm_structure
import json
from src.helper.helper_function import clean_model_json , apply_default_config_to_dynamic_email
from fastapi.responses import JSONResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_email(data: dict):
    print(data)
    
    # Convert the dictionary to a string for the prompt
    data_str = json.dumps(data)
    inputs = {"messages": [{"role": "user", "content":"""Generate a fully dynamic email layout for the following details:""" + data_str}]}

    response = agent.invoke(inputs)

    json_string = response['structured_response'].model_dump_json(indent=2 , by_alias=True ,exclude_none=True)
    

    data = json.loads(json_string)
    final_data = apply_default_config_to_dynamic_email(data)

    return final_data

class GenerateRequest(BaseModel):
    emailType: str
    purpose: str
    tone: str
    targetAudience: str
    keyPoints: str
    additionalDetails: str

@app.post("/generate")
async def generate(request: GenerateRequest):
    query = {}
    query['emailType'] = request.emailType 
    query['purpose'] = request.purpose
    query['tone'] = request.tone
    query['targetAudience'] = request.targetAudience
    query['keyPoints'] = request.keyPoints
    query['additionalDetails'] = request.additionalDetails
    print(query)

    content= generate_email(request.model_dump())
    return JSONResponse(content=content, status_code=200)

