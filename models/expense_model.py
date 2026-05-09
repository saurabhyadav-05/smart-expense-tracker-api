from mongoengine import Document,StringField,FloatField

class Expense(Document):
    title = StringField(required=True)
    amount = FloatField(required=True)
    category = StringField(required=True)