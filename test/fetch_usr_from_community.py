import requests

BASE = "http://127.0.0.1:5000"

payload = {
    "community_id":"6a0d5a03a4f9e66563c207be",
    "page":2
}

r = requests.post(
    f"{BASE}/admin/community",
    json=payload
)

print(r.status_code)
print(r.json())