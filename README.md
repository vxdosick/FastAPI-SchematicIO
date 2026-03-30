# SchematicIO

### Information about the project
1. The project uses Python version 3.12.12.

### Main stack and other architectures
1. Data Structures - pydantic
2. Web protocol - RESTAPI
3. Code versioning - git, github
4. API - AI Integration
5. Build tools - uv
6. Cloud - Render.com

### Useful commands
0. Environment creating and project setup
```bash
uv init
```
1. Install before starting (if requirements.txt is exist)
```bash
uv sync
```
2. Start server
```bash
uvicorn src.main:app --reload
```