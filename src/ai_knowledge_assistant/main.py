from fastapi import FastAPI

app = FastAPI(
    title="AI Knowledge Assistant",
    description="An AI-powered knowledge assistant that provides information and answers to user queries.",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}