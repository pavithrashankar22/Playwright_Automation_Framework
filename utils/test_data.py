import json
from pathlib import Path

def load_account_data():
    data_path=Path(__file__).parent.parent / "test_data" / "account_data.json"
    with open(data_path, "r") as f:
        return json.load(f)
