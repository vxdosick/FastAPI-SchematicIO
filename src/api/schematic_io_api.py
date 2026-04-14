from fastapi import APIRouter, Request, Body
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from src.services.schematic_io_service import SchematicIoService
from src.schemas.schematic_io_schema import SchematicRequest
from core.config import STATIC_DIR

templates = Jinja2Templates(directory=STATIC_DIR / "templates")
router = APIRouter(prefix="/api")

@router.post("/schematic_io_block", response_class=HTMLResponse)
async def schematic_io(request: Request, data: SchematicRequest):
    elements = SchematicIoService.ai_request(data.text)
    html_block = SchematicIoService.build_schema(elements)
    return html_block

@router.post("/schematic_io_elements", response_class=JSONResponse)
async def schematic_io(request: Request, data: SchematicRequest):
    elements = SchematicIoService.ai_request(data.text)
    return elements