import json
from typing import List, Literal, Optional, Any
from pydantic import BaseModel, Field, ConfigDict, alias_generators


class BaseConfigModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=alias_generators.to_camel,
        populate_by_name=True,
        extra='ignore'
    )

class Configuration(BaseConfigModel):
    width: int =  Field(description = "Choose width according to button text content button text must be in oneline") 
    visibility: Optional[Literal["mobile" , "all" ]] = None
    text_size: int = Field(description="Size of text in pixels", default=16)
    text_color: str = Field(description="Color of the text in RGB or HEX", default="rgb(0, 0, 0)")   
    button_color : str = Field(description="Color of the button in liner-gredient or RGB or HEX")
    bg_color: str = Field(description="Background color in RGBA or HEX", default="rgba(0,0,0,0)")
    border_radius: int = Field(description="Border radius in pixels use this in button only" ,default=0)
    image_radius: int = Field(description="Image radius in pixels use this in image only" ,default=0)
    latter_spacing: int = Field(description="Latter spacing in pixels use this in text only" ,default=0)
    border_color: str = Field(description="Border color in RGBA or HEX", default="rgba(0,0,0,0)")
    border_width: int = Field(description="Border width in pixels", default=0)
    font_weight: int = Field(description="Font weight in pixels", default=400)
    

# --- Field Values ---
class BaseFieldValue(BaseConfigModel):
    id: str =  Field(description="Unique ID comtain random string of 8 characters including numerical and small alphabets and the lenth should be excet 8 characters")
    sub_type: str
    configuration: Configuration = Field(alias='Configuration')


class TextFieldValue(BaseFieldValue):
    text: str

class ImageFieldValue(BaseFieldValue):
    url: str

class ButtonFieldValue(BaseFieldValue):
    text: str

class DividerFieldValue(BaseFieldValue):
    pass

class FieldValueContainer(BaseModel):
    text: Optional[TextFieldValue] = None
    img: Optional[ImageFieldValue] = None
    button: Optional[ButtonFieldValue] = None
    divider: Optional[DividerFieldValue] = None


class FieldArrayEntry(BaseConfigModel):
    id: str =  Field(description="Unique ID comtain random string of 8 characters including numerical and small alphabets and the lenth should be excet 8 characters")
    icon: str
    label: str
    name: str
    type: str
    field_value: FieldValueContainer

class ColConfig(BaseConfigModel):
    spacing: int = 16
    max_width: int
    background_color: str = Field(description="Background color in RGBA You can choose any color of background According to the email template's UI", default="rgba(255,255,255,1)")
    background_image: str = Field(description="Background image URL Use image_search tool to get image URL", default=None)
    border_color: str = Field(description="Border color in RGBA You can choose any color of border According to the email template's UI", default="rgba(255,255,255,1)")
    border_radius: int = Field(description="Border radius in pixels", default=0)
    border_width: int = Field(description="Border width in pixels", default=0)

class FieldDetail(BaseConfigModel):
    id: str =  Field(description="Unique ID comtain random string of 8 characters including numerical and small alphabets and the lenth should be excet 8 characters")
    col_config: ColConfig
    field_array: List[FieldArrayEntry]

class RowConfig(BaseConfigModel):
    visibility: Optional[str] = None
    column_layout_category: Optional[str] = None
    background_color: str = Field(description="Background color in RGBA You can choose any color of background According to the email template's UI", default="rgba(255,255,255,1)") 
    background_image: str = Field(description="Background image URL Use image_search tool to get image URL", default=None)

class Row(BaseConfigModel):
    id: str =  Field(description="Unique ID comtain random string of 8 characters including numerical and small alphabets and the lenth should be excet 8 characters")
    row_config: RowConfig
    field_detail: List[FieldDetail]

class DataModel(BaseModel):
    field_list: List[Row]
    name: str = Field(description="Name of the email Template")
    subject: str = Field(description="Subject of the email")
    background_color: str = Field(description="Background color in RGBA You can choose any color of background According to the email template's UI", default="rgba(255,255,255,1)") 
