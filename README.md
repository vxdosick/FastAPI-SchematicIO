# SchematicIO

### Information about the project
1. The project uses Python version 3.12.12.
2. ...

### Main stack and other architectures
1. Project Architectures - fastapi-mvc
2. Data Structures - pydantic
3. Web protocol - RESTAPI
4. Application assembly - Docker
5. Code versioning - git, github
6. API - AI Integration
7. Build tools - uv
8. Testing - ...
9. Utils - ...
10. Cloud - ...

### Additional stack (may be not used)
1. ORM - SQLAlchemy
2. Auth - Custom auth
3. Admin Panels - FastAPI Admin
4. DataBases - PostgreSQL
5. MemoryBases - Redis

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
3. Ngrok starting (to expose local server for testing webhooks or remote access)
```bash
ngrok http 8000
```