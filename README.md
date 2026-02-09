# SchematicIO

### Information about the project
1. The project uses Python version 3.12.12.
2. ...

### Main stack and other architectures
Project Architectures - fastapi-mvc
Data Structures - pydantic
Web protocol - RESTAPI
Application assembly - Docker
Code versioning - git, github
API - AI Integration
Build tools - uv
Testing - ...
Utils - ...
Cloud - ...

### Additional stack (may be not used)
ORM - SQLAlchemy
Auth - Custom auth
Admin Panels - FastAPI Admin
DataBases - PostgreSQL
MemoryBases - Redis

### Useful commands
0. Environment creating and project setup
```bash
uv init
```
```bash
uv venv .venv
```
1. Install before starting (if requirements.txt is exist)
```bash
uv sync
```
2. Start server
```bash
uvicorn server.main:app --reload
```
3. Ngrok starting (to expose local server for testing webhooks or remote access)
```bash
ngrok http 8000
```