from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.auth import get_current_user
import random

router = APIRouter()


@router.get("/", response_model=list[schemas.AIModelOut])
def get_models(db: Session = Depends(get_db),
               current_user: models.User = Depends(get_current_user)):
    return db.query(models.AIModel).all()


@router.post("/register", response_model=schemas.AIModelOut)
def register_model(model: schemas.AIModelCreate,
                   db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_user)):
    existing = db.query(models.AIModel).filter(
        models.AIModel.name == model.name
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Model name already exists")
    new_model = models.AIModel(
        name=model.name,
        version=model.version,
        endpoint_url=model.endpoint_url,
        status="online",
        latency=round(random.uniform(50, 200), 2),
        cpu_load=round(random.uniform(20, 80), 2),
        owner=current_user.username
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model


@router.get("/{model_id}/status", response_model=schemas.AIModelOut)
def get_model_status(model_id: int,
                     db: Session = Depends(get_db),
                     current_user: models.User = Depends(get_current_user)):
    model = db.query(models.AIModel).filter(
        models.AIModel.id == model_id
    ).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    model.latency = round(random.uniform(50, 300), 2)
    model.cpu_load = round(random.uniform(20, 95), 2)
    db.commit()
    db.refresh(model)
    return model


@router.post("/{model_id}/predict")
def predict(model_id: int,
            db: Session = Depends(get_db),
            current_user: models.User = Depends(get_current_user)):
    model = db.query(models.AIModel).filter(
        models.AIModel.id == model_id
    ).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    if model.status == "offline":
        raise HTTPException(status_code=400, detail="Model is offline")
    return {
        "model": model.name,
        "version": model.version,
        "prediction": round(random.uniform(0, 1), 4),
        "confidence": f"{round(random.uniform(70, 99), 1)}%",
        "latency_ms": round(random.uniform(50, 300), 2)
    }


@router.delete("/{model_id}")
def delete_model(model_id: int,
                 db: Session = Depends(get_db),
                 current_user: models.User = Depends(get_current_user)):
    model = db.query(models.AIModel).filter(
        models.AIModel.id == model_id
    ).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    if model.owner != current_user.username:
        raise HTTPException(status_code=403, detail="Not your model")
    db.delete(model)
    db.commit()
    return {"message": f"{model.name} deleted successfully"}
