from pydantic import BaseModel,Field
from typing import Optional
class TaskModel(BaseModel):
    ID:int
    Title: str
    Description: str = Field(None)
    Completed: bool = False

class updateTaskModel(BaseModel): # when using model object is always a dictionary
    Title : Optional[str] = Field(None) 
    Description: Optional[str] = Field(None)
    Completed: Optional[bool] = Field(None)
