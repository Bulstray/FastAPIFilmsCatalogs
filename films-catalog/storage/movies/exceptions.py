class MovieBaseError(Exception):
    """
    Base exception for short url CRUD actions.
    """


class MovieAlreadyExists(MovieBaseError):
    """
    Raised on short url creation if such slug already exists.
    """
