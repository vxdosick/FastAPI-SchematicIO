from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Variables
ROOT_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = ROOT_DIR / "static"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
NGROK_AUTHTOKEN=os.getenv("NGROK_AUTHTOKEN")