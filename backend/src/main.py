from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Account(BaseModel):
    name: str
    email: str
    password: str


@app.post("/api/account")
def create_account(account: Account):
    return {"message": "Account created successfully"}


@app.get("/")
def hello_world():
    return {"message": "Hello World"}
