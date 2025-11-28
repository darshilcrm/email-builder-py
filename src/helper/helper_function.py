import copy
from src.utils.default_values import *
import os
from langchain.tools import tool
import requests

def apply_default_config_to_dynamic_email(email_json):
    """
    Injects default rowConfig, colConfig, and field Configuration
    into the dynamically generated field_list JSON.
    """
    output = copy.deepcopy(email_json)


    for row in output.get("field_list", []):

        temp = {**DefaultValues.DEFAULT_ROW_CONFIG, **row['rowConfig']}
        row["rowConfig"] = temp


        for col in row.get("fieldDetail", []):

            temp =  {**DefaultValues.DEFAULT_COL_CONFIG, **col['colConfig']}
            col["colConfig"] = temp


            for field in col.get("fieldArray", []):
                field_type = field.get("type")
                field_value = field.get("fieldValue", {})

                # TEXT FIELD
                if field_type == "text" and "text" in field_value:

                    temp = {**DefaultValues.DEFAULT_CONFIGURATION, **DefaultValues.DEFAULT_TEXT_CONFIG,**field_value["text"]["Configuration"]}
                    field_value["text"]["Configuration"] = temp
                    

                # IMAGE FIELD
                elif field_type == "image" and "img" in field_value:
                    temp = {**field_value["img"]["Configuration"] , **DefaultValues.DEFAULT_CONFIGURATION, **DefaultValues.DEFAULT_IMAGE_CONFIG}
                    field_value["img"]["Configuration"] = temp

                # BUTTON FIELD
                elif field_type == "button" and "button" in field_value:
                    temp = {**DefaultValues.DEFAULT_CONFIGURATION, **DefaultValues.DEFAULT_BUTTON_CONFIG,**field_value["button"]["Configuration"]}
                    field_value["button"]["Configuration"] = temp

                # DIVIDER FIELD
                elif field_type == "divider" and "divider" in field_value:
                    temp = {**DefaultValues.DEFAULT_CONFIGURATION,**DefaultValues.DEFAULT_DIVIDER_CONFIG, **field_value["divider"]["Configuration"]}
                    field_value["divider"]["Configuration"] = temp

    return output



def clean_model_json(raw_text: str) -> str:
    """
    Remove markdown code fences like ```json or ``` and return raw JSON.
    """
    cleaned = raw_text.strip()

    # Remove ```json ... ```
    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```json", "").replace("```", "").strip()

    return cleaned


@tool
def image_search(query :str) -> str:
    """
    Uses Unsplash API to perform an image search and returns the URL of the first image result.
    """
    access_key = os.getenv("ACCESS_key")

    response = requests.get(f"https://api.unsplash.com/search/photos?page=1&query={query}&client_id={access_key}")

    result = response.json()

    return result['results']
