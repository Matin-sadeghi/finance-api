
from app.models.transaction import Transaction
from app.extensions import db

def create_transaction(user_id :int , data:dict) -> Transaction:

    transaction = Transaction(
        amount=data["amount"],
        type=data["type"],
        category=data["category"],
        description=data.get("description"),
        date=data["date"],
        user_id=user_id
    )

    db.session.add(transaction)
    db.session.commit()

    return transaction