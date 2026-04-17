from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from database import get_db

router = APIRouter(tags=["AI"])


@router.get("/ai")
def ai(question: str, db: Session = Depends(get_db)):
    q = question.lower()

    transactions = db.query(models.Transaction).all()
    clients = db.query(models.Client).all()

    revenue = sum(t.amount for t in transactions if t.type == "revenue")
    expenses = sum(t.amount for t in transactions if t.type == "expense")
    profit = revenue - expenses

    if "impot" in q or "fiscal" in q or "taxe" in q:
        return {
            "answer": "Contexte algérien : vérifiez vos échéances G12, G50 et G1, et anticipez vos déclarations avant la date limite."
        }

    if "profit" in q or "bénéfice" in q or "benefice" in q:
        return {
            "answer": f"Votre bénéfice estimé actuel est de {profit} DZD. Surveillez vos charges pour améliorer votre marge."
        }

    if "client" in q or "marketing" in q:
        return {
            "answer": f"Vous avez actuellement {len(clients)} client(s). Je recommande une campagne ciblée ou un programme de fidélité."
        }

    if "depense" in q or "charge" in q:
        return {
            "answer": f"Vos charges estimées sont de {expenses} DZD. Analysez les postes les plus lourds pour optimiser votre trésorerie."
        }

    if "revenu" in q or "vente" in q:
        return {
            "answer": f"Vos revenus estimés sont de {revenue} DZD. Pensez à fidéliser vos meilleurs clients et augmenter la récurrence."
        }

    if "juridique" in q or "contrat" in q or "document" in q:
        return {
            "answer": "Utilisez le module juridique pour centraliser vos contrats, statuts, pièces administratives et litiges."
        }

    return {
        "answer": "Je suis votre assistant Affairek. Je peux vous aider en fiscalité, comptabilité, marketing, juridique et gestion."
    }