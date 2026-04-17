# Affairek V4 — Prototype SaaS de Gestion Intelligente

## Présentation

**Affairek** est un prototype de plateforme intelligente de gestion intégrée, conçu pour :

- les PME
- les micro-entreprises
- les entrepreneurs
- les professions libérales
- les cabinets comptables

L’objectif est de centraliser dans une seule interface :

- la **comptabilité**
- la **fiscalité**
- le **CRM**
- le **marketing**
- le **juridique**
- l’**assistance intelligente par IA**

---

# Fonctionnalités principales

## 1. Profil Entreprise / Profil Fiscal
L’utilisateur peut enregistrer :

- Nom de l’entreprise
- NIN
- NIF
- NIS
- Activité
- Article d’imposition
- Wilaya
- CPI
- Régime fiscal
- Mode d’utilisation :
  - Entrepreneur
  - Cabinet comptable

---

## 2. Dashboard Global
Le tableau de bord permet de visualiser :

- Revenus
- Dépenses
- Profit
- Cashflow
- Nombre de clients
- Alertes fiscales

---

## 3. Comptabilité
Le module comptable permet :

- d’ajouter des revenus
- d’ajouter des dépenses
- de catégoriser les transactions
- de visualiser un mini pré-bilan
- de détecter certaines dépenses anormales

---

## 4. Fiscalité
Le module fiscal permet :

- d’afficher un calendrier fiscal
- de suivre les obligations déclaratives
- de simuler des pénalités de retard
- de marquer une déclaration comme payée
- d’exporter une estimation financière

---

## 5. CRM & Gestion Client
Le module CRM permet :

- d’ajouter des clients
- d’enregistrer leurs coordonnées
- d’ajouter un historique / notes client

---

## 6. Marketing
Le module marketing permet :

- de créer des campagnes
- d’obtenir des idées marketing automatiques
- de générer des idées de contenu

---

## 7. Juridique
Le module juridique permet :

- d’archiver des documents
- de catégoriser les documents
- de suivre des litiges / contentieux

---

## 8. Mode Cabinet Comptable
Le mode cabinet permet :

- de gérer les documents manquants des clients
- de suivre les pièces reçues
- de maintenir une checklist cabinet

---

## 9. AI Business Copilot
Le copilote IA permet de répondre à des questions sur :

- la fiscalité
- la comptabilité
- les dépenses
- les revenus
- le marketing
- la gestion
- les documents juridiques

---

# Stack Technique

## Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Frontend
- HTML
- CSS
- JavaScript
- Chart.js

---

# Structure du projet

```text
affairek_v4/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── __init__.py
│   └── routes/
│       ├── __init__.py
│       ├── company.py
│       ├── transactions.py
│       ├── clients.py
│       ├── analytics.py
│       ├── fiscal.py
│       ├── marketing.py
│       ├── juridique.py
│       ├── cabinet.py
│       └── ai.py
│
frontend/
│
├── dashboard.html
├── assets/
│   ├── logo.png
│   ├── logo_small.png
│   └── icon.png
│
├── requirements.txt
├── install_windows.bat
└── README.md