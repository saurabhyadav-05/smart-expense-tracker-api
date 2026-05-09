from pydantic import BaseModel

class ExpenseSchema(BaseModel):
    title:str
    amount:float
    category:str