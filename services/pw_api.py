import requests

from services.auth import get_token

UPLOAD_URL = "https://api.penpencil.co/v1/files"


def upload_file(filepath):

    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with open(filepath, "rb") as f:

        files = {
            "image": f
        }

        r = requests.post(
            UPLOAD_URL,
            headers=headers,
            files=files,
            timeout=120
        )

    r.raise_for_status()

    return r.json()
