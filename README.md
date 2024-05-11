# Simple dockerized FastAPI with tests

Features:
1. Dockerized with nginx and uvicorn
2. X-Request-ID requires
3. Has a logmiddleware for json logging
4. Uses pydantic and msgspec for models 
5. Has a test infrastructure - dockerized functional test, unit test.

Build with docker-compose
```bash 
docker compose up --build -d
```

Test functional
```bash 
cd tests/functional
docker compose up -f docker-compose-api.yml --build -d
docker compose up -f docker-compose-tests.yml --build
```