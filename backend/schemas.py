from pydantic import BaseModel
from typing import Optional


# ======================================
# PROFIL ENTREPRISE
# ======================================

class CompanyProfileBase(BaseModel):
    company_name: str
    nin: Optional[str] = ""
    nif: Optional[str] = ""
    nis: Optional[str] = ""
    activity: Optional[str] = ""
    tax_article: Optional[str] = ""
    wilaya: Optional[str] = ""
    cpi: Optional[str] = ""
    tax_regime: Optional[str] = ""
    mode: Optional[str] = "entrepreneur"


class CompanyProfileCreate(CompanyProfileBase):
    pass


class CompanyProfile(CompanyProfileBase):
    id: int

    class Config:
        orm_mode = True


# ======================================
# TRANSACTIONS
# ======================================

class TransactionBase(BaseModel):
    type: str
    amount: float
    description: Optional[str] = ""
    category: Optional[str] = "general"


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True


# ======================================
# CLIENTS
# ======================================

class ClientBase(BaseModel):
    name: str
    email: Optional[str] = ""
    phone: Optional[str] = ""
    history: Optional[str] = ""


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True


# ======================================
# CAMPAGNES
# ======================================

class CampaignBase(BaseModel):
    title: str
    message: str
    channel: Optional[str] = "email"


class CampaignCreate(CampaignBase):
    pass


class Campaign(CampaignBase):
    id: int

    class Config:
        orm_mode = True


# ======================================
# DOCUMENTS JURIDIQUES
# ======================================

class DocumentBase(BaseModel):
    name: str
    category: Optional[str] = "administratif"
    description: Optional[str] = ""
    content: Optional[str] = ""


class DocumentCreate(DocumentBase):
    pass


class Document(DocumentBase):
    id: int

    class Config:
        orm_mode = True


# ======================================
# LITIGES
# ======================================

class LitigeBase(BaseModel):
    title: str
    description: Optional[str] = ""
    status: Optional[str] = "ouvert"


class LitigeCreate(LitigeBase):
    pass


class Litige(LitigeBase):
    id: int

    class Config:
        orm_mode = True


# ======================================
# FISCAL
# ======================================

class TaxDeclarationBase(BaseModel):
    tax_name: str
    due_date: str
    status: Optional[str] = "pending"
    estimated_amount: Optional[float] = 0.0


class TaxDeclarationCreate(TaxDeclarationBase):
    pass


class TaxDeclaration(TaxDeclarationBase):
    id: int

    class Config:
        orm_mode = True


# ======================================
# CABINET
# ======================================

class CabinetTaskBase(BaseModel):
    client_name: str
    document_required: str
    received: Optional[bool] = False


class CabinetTaskCreate(CabinetTaskBase):
    pass


class CabinetTask(CabinetTaskBase):
    id: int

    class Config:
        orm_mode = True