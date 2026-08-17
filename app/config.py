from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent.parent

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "docgenius-development-secret-change-me")
    UPLOAD_FOLDER = str(ROOT / "uploads")
    OUTPUT_FOLDER = str(ROOT / "outputs")
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024
