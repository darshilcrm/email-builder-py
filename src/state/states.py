import json
from typing import List, Literal, Optional, Any
from fastapi import background
from pydantic import BaseModel, Field, ConfigDict, alias_generators


class BaseConfigModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=alias_generators.to_camel,
        populate_by_name=True,
        extra='ignore'
    )

class Configuration(BaseConfigModel):
    width: int = None 
    visibility: Optional[Literal["mobile" , "all" ]] = None
    text_size: int = Field(description="Size of text in pixels", default=16)
    text_color: str = Field(description="Color of the text in RGB or HEX", default="rgb(0, 0, 0)")   
    button_color : str = Field(description="Color of the button in RGB or HEX")
    bg_color: Optional[str] = Field(description="Background color in RGBA or HEX", default="rgba(0,0,0,0)")
    border_radius: Optional[int] = Field(description="Border radius in pixels use this in button only")
   
# --- Field Values ---
class BaseFieldValue(BaseConfigModel):
    id: str
    sub_type: str
    configuration: Configuration = Field(alias='Configuration')


class TextFieldValue(BaseFieldValue):
    text: str

class ImageFieldValue(BaseFieldValue):
    url: str

class ButtonFieldValue(BaseFieldValue):
    text: str
    button_link: str = ""

class DividerFieldValue(BaseFieldValue):
    pass

class FieldValueContainer(BaseModel):
    text: Optional[TextFieldValue] = None
    img: Optional[ImageFieldValue] = None
    button: Optional[ButtonFieldValue] = None
    divider: Optional[DividerFieldValue] = None


class FieldArrayEntry(BaseConfigModel):
    id: str
    icon: str
    label: str
    name: str
    type: str
    field_value: FieldValueContainer

class ColConfig(BaseConfigModel):
    spacing: int = 16
    max_width: int

class FieldDetail(BaseConfigModel):
    id: str
    col_config: ColConfig
    field_array: List[FieldArrayEntry]

class RowConfig(BaseConfigModel):
    visibility: Optional[str] = None
    column_layout_category: Optional[str] = None
    background_color: str = Field(description="Background color in RGBA", default="rgba(0,0,0,0)") 

class Row(BaseConfigModel):
    id: str
    row_config: RowConfig
    field_detail: List[FieldDetail]

class DataModel(BaseModel):
    field_list: List[Row]
