from unittest.mock import patch
from app.services.auth_service import register_user,login_user
import pytest
from app.services.exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError
from werkzeug.security import generate_password_hash

@patch("app.services.auth_service.generate_password_hash")
@patch("app.services.auth_service.User")
@patch("app.services.auth_service.db")
def test_register_user_success(mock_db, mock_user, mock_hash):
    mock_user.query.filter_by.return_value.first.return_value = None
    mock_hash.return_value = "hashed-password"

    expected_user = mock_user.return_value

    result = register_user("test@example.com", "password123")

    mock_hash.assert_called_once_with("password123")
    mock_user.assert_called_once_with(
        email="test@example.com",
        password="hashed-password",
    )
    mock_db.session.add.assert_called_once_with(expected_user)
    mock_db.session.commit.assert_called_once()
    assert result == expected_user


@patch("app.services.auth_service.generate_password_hash")
@patch("app.services.auth_service.User")
@patch("app.services.auth_service.db")
def test_register_user_email_already_exists(mock_db, mock_user, mock_hash):
    mock_user.query.filter_by.return_value.first.return_value = mock_user


    with pytest.raises(EmailAlreadyRegisteredError):
        register_user("test@example.com", "password123")


    mock_hash.assert_not_called()
    mock_user.assert_not_called()
    mock_db.session.add.assert_not_called()
    mock_db.session.commit.assert_not_called()


@patch("app.services.auth_service.check_password_hash")
@patch("app.services.auth_service.User")
def test_login_user_success(mock_user,mock_check_password):
    user = mock_user.return_value
    user.password = "hashed-password"

    mock_user.query.filter_by.return_value.first.return_value = user
    mock_check_password.return_value = True

    result = login_user("test@example.com", "password123")

    mock_check_password.assert_called_once_with(
        "hashed-password",
        "password123",
    )
    assert result == user

@patch("app.services.auth_service.check_password_hash")
@patch("app.services.auth_service.User")
def test_login_user_wrong_password(mock_user, mock_check_password):
    user = mock_user.return_value
    user.password = "hashed-password"

    mock_user.query.filter_by.return_value.first.return_value = user
    mock_check_password.return_value = False

    with pytest.raises(InvalidCredentialsError):
        login_user("test@example.com", "wrong-password")

    mock_check_password.assert_called_once_with(
        "hashed-password",
        "wrong-password",
    )

@patch("app.services.auth_service.check_password_hash")
@patch("app.services.auth_service.User")
def test_login_user_user_not_found(mock_user, mock_check_password):
    mock_user.query.filter_by.return_value.first.return_value = None

    with pytest.raises(InvalidCredentialsError):
        login_user("unknown@example.com", "password123")

    mock_check_password.assert_not_called()

