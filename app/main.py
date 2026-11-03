from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to PHANTOM API"}


@app.get("/health", tags=["health"], summary="Check application health")
def health_check():
    return {"status": "ok", "service": "phantom"}