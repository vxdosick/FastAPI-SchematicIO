from fastapi import APIRouter, Request, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.services.schematic_io_service import SchematicIoService
from core.config import STATIC_DIR
from pydantic import BaseModel

templates = Jinja2Templates(directory=STATIC_DIR / "templates")
router = APIRouter(prefix="/api")

class SchematicRequest(BaseModel):
    text: str

@router.post("/schematic_io_api", response_class=HTMLResponse)
async def schematic_io(request: Request, payload: SchematicRequest):
    elements = SchematicIoService.ai_request(payload.text)
    html_block = SchematicIoService.build_schema(elements)
    return html_block