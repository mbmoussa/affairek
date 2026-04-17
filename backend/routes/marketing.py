from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(tags=["Marketing"])


@router.post("/marketing/campaign")
def create_campaign(campaign: schemas.CampaignCreate, db: Session = Depends(get_db)):
    new_campaign = models.Campaign(**campaign.dict())
    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)
    return {"message": "Campagne créée", "data": new_campaign.__dict__}


@router.get("/marketing/campaigns")
def get_campaigns(db: Session = Depends(get_db)):
    return db.query(models.Campaign).all()


@router.get("/marketing/ai")
def marketing_ai(db: Session = Depends(get_db)):
    clients_count = db.query(models.Client).count()

    if clients_count < 5:
        return {"idea": "Lancer une promotion ciblée pour attirer plus de clients"}
    return {"idea": "Créer un programme de fidélité pour vos meilleurs clients"}


@router.get("/marketing/content_ideas")
def content_ideas():
    return [
        "Publier un conseil fiscal simple pour PME",
        "Partager un avant/après de gestion financière",
        "Créer une publication sur les erreurs fiscales fréquentes",
        "Publier une offre promotionnelle de services"
    ]