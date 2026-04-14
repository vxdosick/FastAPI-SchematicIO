# SchematicIO

### Quick Summary
SchematicIO is an AI-driven service that transforms unstructured text (like scientific articles) into interactive, visual knowledge graphs. 
It bridges the gap between LLM logic extraction and frontend visualization using Cytoscape.js.

### Information about the project
1. The project uses Python version 3.12.12.
2. The launch uses Ngrok for a global link.

### Key Features
- AI-powered text analysis and logic extraction.
- Dynamic Cytoscape.js graph generation.
- Fully responsive embedded widgets.
- CORS enabled for cross-origin integration.

### Main stack and other architectures
1. Server framework - FastAPI + uvicorn
2. Data Validation & Schemas - pydantic
3. Web protocol - RESTAPI
4. Code versioning - git, github
5. API - LLM Integration (OpenRouter / GPT)
6. Build tools - uv
7. Cloud - Render.com

### Architecture & Workflow
User submits text → FastAPI validates via Pydantic → AI Service fetches structured graph from OpenRouter (GPT-4o-mini) → Backend transforms data into Cytoscape.js compatible HTML/JSON → Response returned to client.

### Endpoints
1. Returns ready-to-use HTML/JS component.
```bash
/api/schematic_io_block
```
2. Returns raw JSON for custom frontend integration.
```bash
/api/schematic_io_elements
```

### .env variables
Before running the script, make sure you have specified all variables and secrets.
```bash
OPENROUTER_API_KEY=...
NGROK_AUTHTOKEN=...
```

### Useful commands
0. Environment creation and project setup
```bash
uv init
```
1. Install before starting (if requirements.txt exists)
```bash
uv sync
```
2. Start server
- development mode
```bash
uvicorn src.main:app --reload
```
- production mode
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```
3. API requests
```bash
curl -X 'POST' \
  'https://valorie-nonpsychiatric-gwendolyn.ngrok-free.dev/api/schematic_io_block' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Python is a programming language used for web development and AI."}'
```
```bash
curl -X 'POST' \
  'https://valorie-nonpsychiatric-gwendolyn.ngrok-free.dev/api/schematic_io_elements' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Python is a programming language used for web development and AI."}'
```