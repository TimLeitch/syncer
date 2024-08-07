from fastapi import FastAPI
from app.api.v1.endpoints import contacts

app = FastAPI()

app.include_router(contacts.router, prefix="/api/v1", tags=["contacts"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Syncer API!"}


@app.get("/health")
def health_check():
    return {"message": "Healthy!"}
