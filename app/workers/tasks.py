from app.workers.celery_app import celery_app

@celery_app.task
def process_event(event):
    print("Processing async event:", event)
    return {"status": "processed", "data": event}