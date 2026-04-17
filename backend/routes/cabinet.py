from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(tags=["Cabinet"])


@router.post("/cabinet/task")
def add_task(task: schemas.CabinetTaskCreate, db: Session = Depends(get_db)):
    new_task = models.CabinetTask(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Tâche ajoutée", "data": new_task.__dict__}


@router.get("/cabinet/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.CabinetTask).all()


@router.post("/cabinet/mark_received")
def mark_received(data: dict, db: Session = Depends(get_db)):
    client_name = data.get("client_name")
    document_required = data.get("document_required")

    task = db.query(models.CabinetTask).filter(
        models.CabinetTask.client_name == client_name,
        models.CabinetTask.document_required == document_required
    ).first()

    if task:
        task.received = True
        db.commit()
        db.refresh(task)
        return {"message": "Document marqué comme reçu"}

    return {"message": "Tâche introuvable"}