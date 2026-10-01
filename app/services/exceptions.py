class EmailAlreadyRegisteredError(Exception):
    """Raised when a user tries to register with an email that is already registered."""
    pass

class InvalidCredentialsError(Exception):
    """Raised when a user provides invalid credentials during login."""
    pass