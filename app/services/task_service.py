from sqlalchemy.orm import Session
from ..models.task import Task
from ..models.user import User
from ..schemas import task_schema, user_schema

def get_tasks(db: Session, current_user: User):
    return db.query(Task).filter(Task.owner_id == current_user.id).all()

def create_task(db: Session, task: task_schema.TaskCreate, current_user: User):
    new_task = Task(**task.dict(), owner_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task