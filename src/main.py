# Imports
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import ngrok

from core.config import STATIC_DIR, NGROK_AUTHTOKEN
from src.api.schematic_io import router

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ngrok startup
async def start_ngrok():
    if not NGROK_AUTHTOKEN:
        logger.warning("NGROK_AUTHTOKEN not found")
        return None

    try:
        listener = await ngrok.forward(
            addr=8000,
            authtoken=NGROK_AUTHTOKEN,
        )
        public_url = listener.url()
        logger.info(f"ngrok tunnel created → {public_url}")
        logger.info(f"All endpoints will be available at: {public_url}/ , {public_url}/docs etc...")
        return public_url

    except Exception as e:
        logger.exception("Failed to start ngrok", exc_info=e)
        return None


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    public_url = await start_ngrok()
    yield

app = FastAPI(title="SchematicIO", lifespan=lifespan)

app.include_router(router)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=str(STATIC_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api_info", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("api_info.html", {"request": request})