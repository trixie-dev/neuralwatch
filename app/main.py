from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth, models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NeuralWatch",
    description="AI Model Monitoring API",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(models.router, prefix="/api/models", tags=["Models"])

@app.get("/")
def root():
    return {"message": "NeuralWatch is running 🧠"}
