from fastapi import FastAPI
from routes import upload, compare

app = FastAPI()

app.include_router(upload.router)
app.include_router(compare.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
