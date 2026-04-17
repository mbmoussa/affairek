from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine

from routes import company
from routes import transactions
from routes import clients
from routes import analytics
from routes import fiscal
from routes import marketing
from routes import juridique
from routes import cabinet
from routes import ai

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Affairek Platform V4")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company.router)
app.include_router(transactions.router)
app.include_router(clients.router)
app.include_router(analytics.router)
app.include_router(fiscal.router)
app.include_router(marketing.router)
app.include_router(juridique.router)
app.include_router(cabinet.router)
app.include_router(ai.router)


@app.get("/")
def root():
    return {"message": "Affairek Platform V4 API running"}