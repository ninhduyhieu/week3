from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SalaryInput(BaseModel):
    gross: float

@router.post("/calculate-net")
def calculate_net_salary(data: SalaryInput):
    bhxh = data.gross * 0.08
    bhyt = data.gross * 0.015
    bhtn = data.gross * 0.01
    insurance_total = bhxh + bhyt + bhtn
    taxable_income = data.gross - insurance_total - 11000000  # Personal deduction
    personal_income_tax = 0

    if taxable_income > 0:
        if taxable_income <= 5000000:
            personal_income_tax = taxable_income * 0.05
        elif taxable_income <= 10000000:
            personal_income_tax = 250000 + (taxable_income - 5000000) * 0.1
        else:
            personal_income_tax = 250000 + 500000 + (taxable_income - 10000000) * 0.15

    net_salary = data.gross - insurance_total - personal_income_tax

    return {
        "gross": data.gross,
        "bhxh": round(bhxh, 2),
        "bhyt": round(bhyt, 2),
        "bhtn": round(bhtn, 2),
        "insurance_total": round(insurance_total, 2),
        "tax": round(personal_income_tax, 2),
        "net": round(net_salary, 2)
    }