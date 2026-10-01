from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db
from app.models.user import User
from app.services.exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError


def register_user(email: str, password: str) -> User | None:
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        raise EmailAlreadyRegisteredError

    password_hash = generate_password_hash(password)

    user = User(
        email=email,
        password=password_hash,
    )

    db.session.add(user)
    db.session.commit()

    return user


def login_user(email: str, password: str) -> User | None:
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        raise InvalidCredentialsError

    return user