from os import getenv

if getenv("TESTING") == "1":
    raise EnvironmentError(
        "Environment is not ready for testing",
    )
