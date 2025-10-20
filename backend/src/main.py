from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from src.encryption import encrypt_data
from src.utils import get_data_path, save_data

app = FastAPI()


class Account(BaseModel):
    name: str
    email: str
    password: str


@app.post("/api/account")
def create_account(account: Account):
    # Encrypt input data
    encrypted_data = encrypt_data(account.model_dump_json())

    # write to a file and
    filename = save_data(encrypted_data, f"{account.name}.txt")

    return {"message": "Account created", "filename": filename}


@app.get("/api/download/{filename}")
async def download_file(filename: str):
    """Download a file from the data folder"""
    filepath = get_data_path(filename)
    return FileResponse(filepath)
