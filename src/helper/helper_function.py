import copy
from src.helper.default_values import *

def apply_default_config_to_dynamic_email(email_json):
    """
    Injects default rowConfig, colConfig, and field Configuration
    into the dynamically generated field_list JSON.
    """
    output = copy.deepcopy(email_json)


    for row in output.get("field_list", []):

        temp = {**DEFAULT_ROW_CONFIG, **row['rowConfig']}
        row["rowConfig"] = temp


        for col in row.get("fieldDetail", []):

            temp =  {**DEFAULT_COL_CONFIG, **col['colConfig']}
            col["colConfig"] = temp


            for field in col.get("fieldArray", []):
                field_type = field.get("type")
                field_value = field.get("fieldValue", {})

                # TEXT FIELD
                if field_type == "text" and "text" in field_value:

                    temp = {**DEFAULT_CONFIGURATION, **DEFAULT_TEXT_CONFIG,**field_value["text"]["Configuration"]}
                    field_value["text"]["Configuration"] = temp
                    

                # IMAGE FIELD
                elif field_type == "image" and "img" in field_value:
                    temp = {**DEFAULT_CONFIGURATION, **DEFAULT_IMAGE_CONFIG, **field_value["img"]["Configuration"]}
                    field_value["img"]["Configuration"] = temp

                # BUTTON FIELD
                elif field_type == "button" and "button" in field_value:
                    temp = {**DEFAULT_CONFIGURATION, **DEFAULT_BUTTON_CONFIG,**field_value["button"]["Configuration"]}
                    field_value["button"]["Configuration"] = temp

                # DIVIDER FIELD
                elif field_type == "divider" and "divider" in field_value:
                    temp = {**DEFAULT_CONFIGURATION,**DEFAULT_DIVIDER_CONFIG, **field_value["divider"]["Configuration"]}
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