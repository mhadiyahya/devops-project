from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "application": "DevOps Project",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
