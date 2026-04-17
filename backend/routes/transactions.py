from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(tags=["Transactions"])


@router.post("/transaction")
def add_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    new_transaction = models.Transaction(**transaction.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return {"message": "Transaction ajoutée", "data": new_transaction.__dict__}


@router.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()


@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()

    revenue = sum(t.amount for t in transactions if t.type == "revenue")
    expenses = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": revenue - expenses
    }