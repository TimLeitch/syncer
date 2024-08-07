from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Syncer API!"}


@app.get("/health")
def health_check():
    return {"message": "Healthy!"}
