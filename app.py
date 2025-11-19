from fastapi import FastAPI
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

def generate_email(data : str):

    query = EMAIL_TEMPLATE_PROMPT + data

    response = llm_structure.invoke(query)

    json_string = response.model_dump_json(indent=2 , by_alias=True ,exclude_none=True) 

    cleane_data = json.loads(clean_model_json(json_string))

    final_data = apply_default_config_to_dynamic_email(cleane_data)

    json_string = json.dumps(final_data, indent=2)

    return final_data


@app.post("/generate-email")
async def generate(query :str):

    content= generate_email(query)
    return JSONResponse(content=content, status_code=200)

