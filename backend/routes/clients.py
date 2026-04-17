from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(tags=["Clients"])


@router.post("/client")
def add_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    new_client = models.Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return {"message": "Client ajouté", "data": new_client.__dict__}


@router.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()