import requests

BASE = "https://data-download-ols5.onrender.com"

r = requests.post(f"{BASE}/admin/save")

print(r.status_code)
print(r.json())