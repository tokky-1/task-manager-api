from pydantic import BaseModel,Field

class TaskModel(BaseModel):
    ID:int
    Title: str
    Description: str = Field(None)
    Completed: bool = False
