from fastapi import FastAPI
from pydantic import BaseModel, Field, validator
from typing import Optional

from preprocessing.core import is_rich, get_notation

from math import log


# FastAPI
app = FastAPI()

MAX_CREDIT = 10000


class ScoringInput(BaseModel):
    montant_credit: int = Field(..., example=2300)
    revenu_fiscal: int = Field(..., example=50000)
    decouvert: bool = Field(..., example=True)
    isf: Optional[bool] = Field(False, example=True)
    banque: Optional[str] = Field('Unknown', example="Crédit mutuel")

    @validator('montant_credit', 'revenu_fiscal')
    def check_positive(cls, amount):
        if amount < 0:
            msg = 'Le montant du crédit et le revenu fiscal doivent être positifs'
            raise ValueError(msg)
        return amount

    @validator('montant_credit')
    def check_max_credit(cls, amount):
        if amount > MAX_CREDIT:
            msg = 'Montant maximal du crédit : {} euros'.format(MAX_CREDIT)
            raise ValueError(msg)
        return amount


@app.post("/scoring/{client_id}")
def get_score(client_id: int, client_details: ScoringInput):

    rich_client = is_rich(client_details.revenu_fiscal)

    proba_non_payment = 0.8 - rich_client * 0.3 \
                            - client_details.isf * 0.4 \
                            + client_details.decouvert * 0.1 \
                            - log(MAX_CREDIT - client_details.montant_credit) / 100
    
    notation = get_notation(proba_non_payment)

    return {
        "client_id": client_id, 
        "banque": client_details.banque,
        "proba_non_payment": proba_non_payment,
        "notation": notation
    }
