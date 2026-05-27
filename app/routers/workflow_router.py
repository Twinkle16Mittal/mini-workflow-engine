import uuid
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Workflow
from app.schemas import WorkflowCreate

router = APIRouter(prefix="/workflow")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def create_workflow(workflow: WorkflowCreate, db: Session = Depends(get_db)):
    webhook_id = str(uuid.uuid4())
    db_workflow = Workflow(name=workflow.name, webhook_path=webhook_id, user_id=1)  # Replace with actual user ID
    db.add(db_workflow)
    db.commit()
    return {"webhook_url": f"/webhook/{webhook_id}"}

