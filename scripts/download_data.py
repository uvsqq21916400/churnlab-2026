import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = (
    "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
    "1fd6fd70906479be1712e64cfc0ea89f58466629/data/Telco-Customer-Churn.csv"
)
EXPECTED_SHA256 = "16320c9c1ec72448db59aa0a26a0b95401046bef5d02fd3aeb906448e3055e91"

csv_path = Path("data/raw/telco.csv")
meta_path = Path("data/raw/telco.source.json")
csv_path.parent.mkdir(parents=True, exist_ok=True)

if not csv_path.exists():
    print(f"Téléchargement depuis {URL}")
    urllib.request.urlretrieve(URL, csv_path)

sha256 = hashlib.sha256(csv_path.read_bytes()).hexdigest()
if sha256 != EXPECTED_SHA256:
    raise ValueError(f"Hash inattendu : {sha256}")

meta = {
    "source_url": URL,
    "sha256": sha256,
    "retrieved_at": datetime.now(timezone.utc).isoformat(),
}
meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
print(json.dumps(meta, indent=2))
