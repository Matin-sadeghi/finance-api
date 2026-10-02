
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

def get_transactions_by_user(user_id: int):
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    return transactions

def get_transaction(user_id:int , transaction_id:int):
    transaction = Transaction.query.filter(Transaction.user_id == user_id , Transaction.id == transaction_id).first()
    return transaction



def update_transaction(transaction: Transaction, data: dict) -> Transaction:
    for key, value in data.items():
        setattr(transaction, key, value)
    db.session.commit()
    return transaction

def delete_transaction(transaction:Transaction)->None:
    db.session.delete(transaction)
    db.session.commit()
