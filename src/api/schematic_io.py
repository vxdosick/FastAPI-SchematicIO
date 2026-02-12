from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.services.schematic_io_service import SchematicIoService
from core.config import STATIC_DIR

templates = Jinja2Templates(directory=STATIC_DIR / "templates")
router = APIRouter(prefix="/api")

@router.post("/schematic_io", response_class=HTMLResponse)
async def schematic_io(request: Request, text: str = Form(...)):

    elements = SchematicIoService.ai_request(text)
    html_block = SchematicIoService.build_schema(elements)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "html_block": html_block}
    )
