from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core import database
from ..schemas import task_schema
from ..services import task_service, auth_service
from ..models import user as user_models

router = APIRouter()

@router.get("/", response_model=list[task_schema.TaskResponse])
def read_tasks(db: Session = Depends(database.get_db), current_user: user_models.User = Depends(auth_service.get_current_user)):
    return task_service.get_tasks(db, current_user)

@router.post("/", response_model=task_schema.TaskResponse)
def create_task(task: task_schema.TaskCreate, db: Session = Depends(database.get_db), current_user: user_models.User = Depends(auth_service.get_current_user)):
    return task_service.create_task(db, task, current_user)