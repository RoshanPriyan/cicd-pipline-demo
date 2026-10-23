
from fastapi import FastAPI

app = FastAPI(title="CI Learning Project")


@app.get("/")
def home():
    return {"message": "Welcome to my CI project"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Roshan"
    }
