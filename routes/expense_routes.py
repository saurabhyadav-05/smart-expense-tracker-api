from fastapi import APIRouter, UploadFile, File
from models.expense_model import Expense
from schemas.expense_schema import ExpenseSchema

import pandas as pd

router = APIRouter()


# ADD EXPENSE
@router.post("/expenses")
def add_expense(expense: ExpenseSchema):

    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )

    new_expense.save()

    return {
        "message": "Expense Added Successfully"
    }


# GET ALL EXPENSES
@router.get("/expenses")
def get_expenses():

    expenses = Expense.objects()

    data = []

    for expense in expenses:

        data.append({
            "id": str(expense.id),
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category
        })

    return data


# UPDATE EXPENSE
@router.put("/expenses/{expense_id}")
def update_expense(expense_id: str, expense: ExpenseSchema):

    existing_expense = Expense.objects(id=expense_id).first()

    if not existing_expense:
        return {
            "message": "Expense Not Found"
        }

    existing_expense.title = expense.title
    existing_expense.amount = expense.amount
    existing_expense.category = expense.category

    existing_expense.save()

    return {
        "message": "Expense Updated Successfully"
    }


# DELETE EXPENSE
@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: str):

    expense = Expense.objects(id=expense_id).first()

    if not expense:
        return {
            "message": "Expense Not Found"
        }

    expense.delete()

    return {
        "message": "Expense Deleted Successfully"
    }


# CSV UPLOAD
@router.post("/upload-csv")
def upload_csv(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    for _, row in df.iterrows():

        expense = Expense(
            title=row["title"],
            amount=row["amount"],
            category=row["category"]
        )

        expense.save()

    return {
        "message": "CSV Uploaded Successfully"
    }