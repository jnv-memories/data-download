from pathlib import Path

AUTH_FILE = Path("auth.txt")
AUTH_FILE2 = Path("auth2.txt")


def get_token():
    if not AUTH_FILE.exists():
        raise FileNotFoundError("auth.txt not found. Create auth.txt and paste your bearer token.")
    token = AUTH_FILE.read_text(encoding="utf-8").strip()
    if token.startswith("Bearer "):
        token = token[7:].strip()
    if not token:
        raise ValueError("auth.txt is empty.")
    return token
def get_token2():
    if not AUTH_FILE2.exists():
        raise FileNotFoundError("auth.txt not found. Create auth.txt and paste your bearer token.")
    token2 = AUTH_FILE2.read_text(encoding="utf-8").strip()
    if token2.startswith("Bearer "):
        token2 = token2[7:].strip()
    if not token2:
        raise ValueError("auth2.txt is empty.")
    return token2


def get_headers():
    return {
        "authorization": f"Bearer {get_token()}"
    }
def get_headers2():
    return {
        "authorization": f"Bearer {get_token2()}"
    }