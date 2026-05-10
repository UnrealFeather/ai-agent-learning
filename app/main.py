from fastapi import FastAPI

app = FastAPI(title="AI Agent Learning Backend")

@app.get("/health")
def health_check():
    return {"status": "ok"}
