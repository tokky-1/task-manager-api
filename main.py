from fastapi import FastAPI,Form
from fastapi import  HTTPException,status
from model import TaskModel
app = FastAPI( title=" Day 2",
                description=" ")
tasks = [ ]

@app.post("/")
def welcome():
    #print(" WELcome to this test page")
    return {" Welcome to this test page"}

@app.post("/health")
def health():
    #print(" WELcome to this test page")
    return{" working just fine"}

@app.post("/Create-Task") # not there shouldn't be spaces in the route name
def create_task(task:TaskModel):
    for t in tasks:
        if t.ID == task.ID:
            raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks.append(task)
    return {"message": "Task created successfully", "task": task}

@app.get("/Read-All")
def read_tasks():
        return tasks

@app.get("/Read-A-Task") 
def read_a_task(id:int):
    for t in tasks:
        if id == tasks.ID:
            return  t

@app.patch("/Update-task")
def update_task(id: int,task:TaskModel):
    for index, t in enumerate(tasks):
        if t["id"] == id:
                tasks[index] = task # overwrite the task
                return {"message": "Task updated successfully", "task": task}
        
    raise HTTPException(status_code=404, detail="Task not found")                 

@app.get("/Delete-Task") 
def delete_a_task(id:int):
    for t in tasks:
        if id == tasks.ID:
            tasks.remove(t)
            return(f"Task with {id} removed")
