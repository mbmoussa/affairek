import openai
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter()

openai.api_key = "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"


@router.get("/ai")
def ai(question: str, db: Session = Depends(get_db)):

    transactions = db.query(models.Transaction).all()
    clients = db.query(models.Client).all()

    revenue = sum(t.amount for t in transactions if t.type == "revenue")
    expenses = sum(t.amount for t in transactions if t.type == "expense")

    prompt = f"""
    Tu es un expert en gestion d'entreprise en Algérie.

    Données:
    - Revenus: {revenue}
    - Dépenses: {expenses}
    - Clients: {len(clients)}

    Question:
    {question}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"answer": response.choices[0].message["content"]}
