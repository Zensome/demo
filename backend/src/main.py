from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from src.encryption import encrypt_data
from src.models import Account
from src.utils import get_data_path, save_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/account")
def create_account(account: Account):
    """
    Encrypts the input data and saves it to a file.
    """
    encrypted_data = encrypt_data(account.model_dump_json())

    filename = save_data(encrypted_data, f"{account.name}.txt")

    return {"message": "Account created", "filename": filename}


@app.get("/api/download/{filename}")
async def download_file(filename: str):
    """Download a file from the data folder"""
    filepath = get_data_path(filename)
    return FileResponse(filepath)
