from app.celery_worker import celery
import time

@celery.task(bind=True, max_retries=3)
def process_webhook(self, payload):
    try:
        print("Processing webhook payload")
        time.sleep(5)
        print(payload)
        return {"status": "completed"}
    except Exception as e:
        print(f"Error processing webhook: {e}")
        raise self.retry(exc=e, countdown=5)