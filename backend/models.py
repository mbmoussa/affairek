from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


# ======================================
# PROFIL ENTREPRISE
# ======================================

class CompanyProfile(Base):
    __tablename__ = "company_profiles"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    nin = Column(String, nullable=True)
    nif = Column(String, nullable=True)
    nis = Column(String, nullable=True)
    activity = Column(String, nullable=True)
    tax_article = Column(String, nullable=True)
    wilaya = Column(String, nullable=True)
    cpi = Column(String, nullable=True)
    tax_regime = Column(String, nullable=True)
    mode = Column(String, default="entrepreneur")


# ======================================
# TRANSACTIONS
# ======================================

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)   # revenue / expense
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, default="general")


# ======================================
# CLIENTS
# ======================================

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    history = Column(String, default="")


# ======================================
# CAMPAGNES MARKETING
# ======================================

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    message = Column(String, nullable=False)
    channel = Column(String, default="email")


# ======================================
# DOCUMENTS JURIDIQUES
# ======================================

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, default="administratif")
    description = Column(String, default="")
    content = Column(String, default="")


# ======================================
# LITIGES / CONTENTIEUX
# ======================================

class Litige(Base):
    __tablename__ = "litiges"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, default="")
    status = Column(String, default="ouvert")


# ======================================
# OBLIGATIONS FISCALES
# ======================================

class TaxDeclaration(Base):
    __tablename__ = "tax_declarations"

    id = Column(Integer, primary_key=True, index=True)
    tax_name = Column(String, nullable=False)
    due_date = Column(String, nullable=False)
    status = Column(String, default="pending")
    estimated_amount = Column(Float, default=0.0)


# ======================================
# MODE CABINET
# ======================================

class CabinetTask(Base):
    __tablename__ = "cabinet_tasks"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    document_required = Column(String, nullable=False)
    received = Column(Boolean, default=False)