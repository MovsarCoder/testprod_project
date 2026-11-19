from fastapi import FastAPI

app = FastAPI(title='test deploy', version="0.1.0", description="test deploy fastapi")


@app.get('/')
def index():
    return {"message": "Hello World!"}



@app.get("/health")
def health():
    return {"status": "ok"}


