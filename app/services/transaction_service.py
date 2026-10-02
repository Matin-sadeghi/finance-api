
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

def get_transactions_by_user(user_id: int,filters:dict):

    query = Transaction.query.filter_by(user_id=user_id)

    if filters.get("type"):
        query = query.filter_by(type=filters["type"])

    if filters.get("category"):
        query = query.filter_by(category=filters["category"])

    if filters.get("start_date"):
        query = query.filter(Transaction.date >= filters["start_date"])

    if filters.get("end_date"):
        query = query.filter(Transaction.date <= filters["end_date"])

    return query.order_by(Transaction.date.desc(),Transaction.id.desc()).paginate(page=filters.get("page", 1), per_page=filters.get("per_page", 10), error_out=False)



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
