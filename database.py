from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()

def connect_db():
    
    connect(db="expenseDB",
            host=os.getenv("MONGO_URL")
        )