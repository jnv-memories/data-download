import requests

BASE = "http://127.0.0.1:5000"

r = requests.get(f"{BASE}/admin/health")

print(r.status_code)
print(r.json())