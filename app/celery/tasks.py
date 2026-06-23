from celery_app import celery

@celery.task
def send_email(email):

    print("Sending email to",email)