import os
from dotenv import load_dotenv

load_dotenv()
DATA_FOLDER = os.getenv("DATA_FOLDER")


def save_data(data: str, filename: str):
    """Saves the data to the file"""
    filepath = os.path.join(DATA_FOLDER, filename)
    with open(filepath, "w") as f:
        f.write(data)
    return filename


def get_data_path(filename: str):
    """Returns the data from the file"""
    filepath = os.path.join(DATA_FOLDER, filename)
    return filepath
