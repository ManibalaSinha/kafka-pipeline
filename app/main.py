from fastapi import FastAPI

from app.api.routes import router

from app.database.db import Base, engine

app = FastAPI(title="Enterprise Data Pipeline", version="1.0.0")

app.include_router(router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")

def home():

    return {"message": "Enterprise Data Pipeline Running"}