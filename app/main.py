from fastapi import FastAPI
import uvicorn
from app.core.config import settings
from app.api.v1 import standing_routes

app = FastAPI()
app.include_router(standing_routes.router, prefix="/standings", tags=["standings"])

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    uvicorn.run(app, host=settings.server_ip, port=settings.port)