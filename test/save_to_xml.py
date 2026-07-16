import requests

BASE = "http://127.0.0.1:5000"

r = requests.post(f"{BASE}/admin/save")

print(r.status_code)
print(r.json())