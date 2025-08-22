from fastapi import FastAPI,Form,Depends
from fastapi import  HTTPException,status
from model import TaskModel,updateTaskModel as UTM
from sqlalchemy.orm import Session
from database.connect import get_db
from database.model import Task

app = FastAPI( title=" Day 2",
                description=" ")


@app.post("/")
def welcome():
    return {" Welcome to this test page"}

@app.post("/health")
def health():
    return{" working just fine"}

@app.post("/Create-Task") # not there shouldn't be spaces in the route name
def create_task(title:str,description:str,db:Session = Depends(get_db)):
    task = Task(title = title,description = description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"message": "Task created successfully",
            "TITLE":title,
            "DESCRIPTION": description}

@app.get("/Read-All")
def read_tasks(db: Session = Depends(get_db)):
        return db.query(Task).all()

@app.get("/Read-A-Task") 
def read_a_task(id:int,db: Session = Depends(get_db)):
    exist= db.query(Task).filter(id == Task.id).first()
    if exist:
         return{
              "ID" : id,
              "TITLE":exist.title,
              "DESCRIPTION": exist.description
         }
    else:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="task doesn't exist")

@app.patch("/Update-task") # when creating an update its best to create a pydantic model for it

def update_task(id: int,updated_data:UTM,db: Session = Depends(get_db)):
    task = db.query(Task).filter(id == Task.id).first()
    
    if not task:
            raise HTTPException(status_code=404, detail="Post not found")

    for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(task, field, value)
        
    db.commit()
    db.refresh(task)
    return task

@app.get("/Delete-Task") 
def delete_a_task(id:int,db: Session = Depends(get_db)):
   exist = db.query(Task).filter(id == Task.id).first()
   
   if not exist:
        raise HTTPException(status_code=404, detail="Post not found")

   db.delete(exist)
   db.commit()
   raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)