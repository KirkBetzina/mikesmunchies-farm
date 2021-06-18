from typing import Optional
from pydantic import BaseModel, Field

class MenuSchema(BaseModel):
    Food: str = Field(...)
    Description: str = Field(...)  
    Price: int = Field(...)

class Config:
    schema_extra = {
        "example" : {
    "Food": "Hot Dogs",
    "Description": "All beef Kosher 1/4lb Grilled Hot Dogs 2 per order. Served with fries",
    "Price": 7.50
        }
    }

class UpdateMenuModel(BaseModel):
    Food: Optional[str] 
    Description: Optional[str]
    Price: Optional[int]    

    class Config:
        schema_extra = {
            "example":{
                "Food" : "1/4lb Kosher Beef Hot Dog",
                "Description": "All beef Kosher Hot Dogs. 2 per order served with fries or butterfly potatoes",
                "Price": 7.50
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}