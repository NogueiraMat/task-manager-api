from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.user import router as user_router


app = FastAPI(
    title="Task Manager API",
    description="Sample FastAPI application for task manager",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Server is on..."}


app.include_router(auth_router, prefix="/api", tags=["Authentication"])
app.include_router(user_router, prefix="/api", tags=["Users"])

