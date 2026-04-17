from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(tags=["Company"])


@router.post("/company/profile")
def save_company_profile(profile: schemas.CompanyProfileCreate, db: Session = Depends(get_db)):
    existing = db.query(models.CompanyProfile).first()

    if existing:
        existing.company_name = profile.company_name
        existing.nin = profile.nin
        existing.nif = profile.nif
        existing.nis = profile.nis
        existing.activity = profile.activity
        existing.tax_article = profile.tax_article
        existing.wilaya = profile.wilaya
        existing.cpi = profile.cpi
        existing.tax_regime = profile.tax_regime
        existing.mode = profile.mode
        db.commit()
        db.refresh(existing)
        return {"message": "Profil entreprise mis à jour", "data": existing.__dict__}

    new_profile = models.CompanyProfile(**profile.dict())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return {"message": "Profil entreprise enregistré", "data": new_profile.__dict__}


@router.get("/company/profile")
def get_company_profile(db: Session = Depends(get_db)):
    profile = db.query(models.CompanyProfile).first()
    if not profile:
        return {}
    return profile