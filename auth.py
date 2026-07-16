from pathlib import Path

AUTH_FILE = Path("auth.txt")


def get_token():
    """
    Reads the bearer token from auth.txt.

    auth.txt may contain either:
        Bearer eyJhbGciOi...
    or just:
        eyJhbGciOi...
    """

    if not AUTH_FILE.exists():
        raise FileNotFoundError(
            "auth.txt not found. Create auth.txt and paste your bearer token."
        )

    token = AUTH_FILE.read_text(encoding="utf-8").strip()

    if token.startswith("Bearer "):
        token = token[7:].strip()

    if not token:
        raise ValueError("auth.txt is empty.")

    return token


def get_headers():
    return {
        "authorization": f"Bearer {get_token()}"
    }