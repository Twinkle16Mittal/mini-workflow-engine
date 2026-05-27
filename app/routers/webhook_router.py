from fastapi import APIRouter, Request
from app.mongodb import mongo_db
from app.tasks import process_webhook
from app.schemas import WebhookPayload
router = APIRouter(prefix="/webhook")

@router.post("/{workflow_id}")
async def receive_webhook(workflow_id: str, payload: WebhookPayload):
    payload = payload.dict()
    await mongo_db.workflow_logs.insert_one({"workflow_id": workflow_id, "payload": payload})
    process_webhook.delay(payload)
    return {"message": "Webhook received and processing started"}