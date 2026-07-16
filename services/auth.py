from pathlib import Path

AUTH_FILE = Path("auth.txt")


def get_token():

    if not AUTH_FILE.exists():
        raise Exception("auth.txt not found")

    token = AUTH_FILE.read_text().strip()

    if token.startswith("Bearer "):
        token = token[7:]

    return token
