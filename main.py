from fastapi import FastAPI
from database import connect_db
from routes.expense_routes import router

app = FastAPI()

connect_db()

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Smart Expense Tracker API Running"
    }
