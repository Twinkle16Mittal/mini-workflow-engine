from fastapi import FastAPI
from app.database import Base, engine
from app.routers.user_router import router as user_router
from app.routers.workflow_router import router as workflow_router
from app.routers.webhook_router import router as webhook_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_router)
app.include_router(workflow_router)
app.include_router(webhook_router)

@app.get("/")
def home():
    return {"message": "Mini Workflow Engine Running"}   