from decimal import Decimal

from sqlalchemy import func

from app.extensions import db
from app.models.transaction import Transaction


def get_financial_summary(user_id:int,start_date=None,end_date=None):
    query = db.session.query(
        Transaction.type,
        func.coalesce(func.sum(Transaction.amount), 0).label("total"),
    ).filter(
        Transaction.user_id == user_id
    )

    if start_date:
        query = query.filter(Transaction.date >= start_date)

    if end_date:
        query = query.filter(Transaction.date <= end_date)

    results = query.group_by(Transaction.type).all()

    totals = {"income": Decimal("0.00"), "expense": Decimal("0.00")}

    for transaction_type, total in results:
        totals[transaction_type] = total

    net_balance = totals["income"] - totals["expense"]

    return {
        "income": totals["income"],
        "expense": totals["expense"],
        "net_balance": net_balance,
    }