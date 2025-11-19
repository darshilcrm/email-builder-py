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
    width: int = None 
    visibility: Optional[Literal["mobile" , "all" ]] = None

# --- Field Values ---
class BaseFieldValue(BaseConfigModel):
    id: str
    sub_type: str
    # Fixed alias issue from previous error
    configuration: Configuration = Field(alias='Configuration')

class TextFieldValue(BaseFieldValue):
    text: str

class ImageFieldValue(BaseFieldValue):
    url: str

class ButtonFieldValue(BaseFieldValue):
    text: str
    button_link: str

class DividerFieldValue(BaseFieldValue):
    pass

class FieldValueContainer(BaseModel):
    text: Optional[TextFieldValue] = None
    img: Optional[ImageFieldValue] = None
    button: Optional[ButtonFieldValue] = None
    divider: Optional[DividerFieldValue] = None

# --- Structure ---
class FieldArrayEntry(BaseConfigModel):
    id: str
    icon: str
    label: str
    name: str
    type: str
    field_value: FieldValueContainer

class ColConfig(BaseConfigModel):
    spacing: int = 16

class FieldDetail(BaseConfigModel):
    id: str
    col_config: ColConfig
    field_array: List[FieldArrayEntry]

class RowConfig(BaseConfigModel):
    visibility: Optional[str] = None
    column_layout_category: Optional[str] = None
    stack_column: Optional[bool] = None

class Row(BaseConfigModel):
    id: str
    row_config: RowConfig
    field_detail: List[FieldDetail]
    stack_column: Optional[bool] = None

class DataModel(BaseModel):
    field_list: List[Row]
