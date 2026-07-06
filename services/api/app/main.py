from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="DevOps Platform API",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "service": "devops-platform-api",
        "status": "running",
    }


@app.get("/health")
async def health():
    return JSONResponse(
        {
            "status": "healthy",
        }
    )


@app.get("/version")
async def version():
    return {
        "version": app.version,
    }