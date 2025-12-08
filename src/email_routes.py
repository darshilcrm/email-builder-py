from pydantic import BaseModel
from fastapi.responses import JSONResponse
from llm.llm import agent
import json
from helper.helper_function import apply_default_config_to_dynamic_email
from fastapi import BackgroundTasks
from langchain_community.callbacks import get_openai_callback
from datetime import datetime
import os
import csv

def token_usages_writer(cb):
    filename = "token_usage_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(filename)
    row = [
        timestamp,
        cb.prompt_tokens,
        cb.completion_tokens,
        cb.reasoning_tokens,
        cb.total_tokens,
        cb.successful_requests,
        cb.total_cost
    ]
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header if file is new
            if not file_exists:
                headers = ["Timestamp","Input Tokens", "Output Tokens", "Reasoning Tokens", "Total Tokens(input + output)", "Successful Requests", "Total Cost (USD)"]
                writer.writerow(headers)
            
            # Write the data
            writer.writerow(row)
        
    except IOError as e:
        print(f"Error writing to file: {e}")
    
class GenerateRequest(BaseModel):
    emailType: str
    purpose: str
    tone: str
    targetAudience: str
    keyPoints: str
    additionalDetails: str

def generate_email(data: dict , background_tasks: BackgroundTasks):
    # Convert the dictionary to a string for the prompt
    data_str = json.dumps(data)
    inputs = {"messages": [{"role": "user", "content":"""Generate a fully dynamic email layout for the following details:""" + data_str}]}

    # response = agent.invoke(inputs)

    with get_openai_callback() as cb:
        response = agent.invoke(inputs)
        

    json_string = response['structured_response'].model_dump_json(indent=2 , by_alias=True ,exclude_none=True)
    

    data = json.loads(json_string)
    final_data = apply_default_config_to_dynamic_email(data)
    

    background_tasks.add_task(token_usages_writer , cb)
    return final_data

async def generate(request: GenerateRequest , background_tasks: BackgroundTasks):
    query = {}
    query['emailType'] = request.emailType 
    query['purpose'] = request.purpose
    query['tone'] = request.tone
    query['targetAudience'] = request.targetAudience
    query['keyPoints'] = request.keyPoints
    query['additionalDetails'] = request.additionalDetails

    content= generate_email(request.model_dump() , background_tasks)
    
    return JSONResponse(content=content, status_code=200)



    