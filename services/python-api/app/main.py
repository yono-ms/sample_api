from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Docker API"}

@app.get("/health")
def health():
    return {"status": "ok"}
