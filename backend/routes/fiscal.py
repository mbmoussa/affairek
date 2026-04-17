from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(tags=["Fiscalité"])


@router.get("/fiscal/init")
def init_fiscal(db: Session = Depends(get_db)):
    existing = db.query(models.TaxDeclaration).count()

    if existing == 0:
        defaults = [
            models.TaxDeclaration(tax_name="G12 IFU", due_date="30/04/2026", status="pending", estimated_amount=0),
            models.TaxDeclaration(tax_name="G50 TVA", due_date="20/03/2026", status="pending", estimated_amount=0),
            models.TaxDeclaration(tax_name="G1 Déclaration Globale", due_date="15/05/2026", status="pending", estimated_amount=0),
        ]
        db.add_all(defaults)
        db.commit()

    return {"message": "Calendrier fiscal initialisé"}


@router.get("/fiscal/calendar")
def calendar(db: Session = Depends(get_db)):
    return db.query(models.TaxDeclaration).all()


@router.post("/fiscal/declaration")
def add_declaration(data: schemas.TaxDeclarationCreate, db: Session = Depends(get_db)):
    declaration = models.TaxDeclaration(**data.dict())
    db.add(declaration)
    db.commit()
    db.refresh(declaration)
    return {"message": "Déclaration ajoutée", "data": declaration.__dict__}


@router.get("/fiscal/alerts")
def alerts(db: Session = Depends(get_db)):
    declarations = db.query(models.TaxDeclaration).all()
    return [
        f"Echéance fiscale : {d.tax_name} le {d.due_date} [{d.status}]"
        for d in declarations
    ]


@router.get("/fiscal/export")
def export_fiscal(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()

    revenue = sum(t.amount for t in transactions if t.type == "revenue")
    expenses = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "revenus": revenue,
        "charges": expenses,
        "benefice_estime": revenue - expenses
    }


@router.get("/fiscal/penalty")
def penalty(days_late: int = 0, amount: float = 0):
    penalty_amount = round(amount * 0.01 * days_late, 2)
    return {
        "days_late": days_late,
        "base_amount": amount,
        "penalty": penalty_amount
    }


@router.post("/fiscal/mark_paid")
def mark_paid(data: dict, db: Session = Depends(get_db)):
    tax_name = data.get("tax")
    declaration = db.query(models.TaxDeclaration).filter(models.TaxDeclaration.tax_name == tax_name).first()

    if declaration:
        declaration.status = "paid"
        db.commit()
        db.refresh(declaration)
        return {"message": "Déclaration marquée comme payée"}

    return {"message": "Déclaration introuvable"}