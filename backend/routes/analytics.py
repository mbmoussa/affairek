from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from database import get_db

router = APIRouter(tags=["Analytics"])


@router.get("/analytics/cashflow")
def cashflow(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()

    revenue = sum(t.amount for t in transactions if t.type == "revenue")
    expenses = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "revenue": revenue,
        "expenses": expenses,
        "cashflow": revenue - expenses
    }


@router.get("/analytics/prebilan")
def prebilan(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()

    revenue = sum(t.amount for t in transactions if t.type == "revenue")
    expenses = sum(t.amount for t in transactions if t.type == "expense")
    profit = revenue - expenses

    margin = 0
    if revenue > 0:
        margin = round((profit / revenue) * 100, 2)

    return {
        "chiffre_affaires": revenue,
        "charges": expenses,
        "benefice": profit,
        "marge_percent": margin
    }


@router.get("/analytics/anomaly")
def anomaly(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    alerts = []

    for t in transactions:
        if t.type == "expense" and t.amount > 3000:
            alerts.append({
                "warning": "Dépense anormale détectée",
                "amount": t.amount,
                "description": t.description
            })

    return alerts


@router.get("/analytics/overview")
def overview(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    clients = db.query(models.Client).all()
    fiscal = db.query(models.TaxDeclaration).all()

    revenue = sum(t.amount for t in transactions if t.type == "revenue")
    expenses = sum(t.amount for t in transactions if t.type == "expense")
    profit = revenue - expenses

    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": profit,
        "cashflow": profit,
        "client_count": len(clients),
        "new_clients_month": len(clients),
        "fiscal_deadlines_count": len(fiscal)
    }