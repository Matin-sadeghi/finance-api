from datetime import datetime, timezone
from app.extensions import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(
            db.Numeric(12,2),
            nullable=False,
        )

    type = db.Column(
        db.String(50),
        nullable=False,
    )

    category = db.Column(
        db.String(50),
        nullable=False,
    )

    description = db.Column(
        db.String(255),
        nullable=True,
    )

    date = db.Column(
        db.Date,
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )