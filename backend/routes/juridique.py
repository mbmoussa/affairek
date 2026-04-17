from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(tags=["Juridique"])


@router.post("/juridique/document")
def add_document(document: schemas.DocumentCreate, db: Session = Depends(get_db)):
    new_doc = models.Document(**document.dict())
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return {"message": "Document ajouté", "data": new_doc.__dict__}


@router.get("/juridique/documents")
def list_documents(db: Session = Depends(get_db)):
    return db.query(models.Document).all()


@router.post("/juridique/litige")
def add_litige(litige: schemas.LitigeCreate, db: Session = Depends(get_db)):
    new_litige = models.Litige(**litige.dict())
    db.add(new_litige)
    db.commit()
    db.refresh(new_litige)
    return {"message": "Litige enregistré", "data": new_litige.__dict__}


@router.get("/juridique/litiges")
def list_litiges(db: Session = Depends(get_db)):
    return db.query(models.Litige).all()