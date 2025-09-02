import json
import re
import os

ABBR_PATH = os.path.join("data", "abbreviation_map.json")

with open(ABBR_PATH, "r") as f:
    abbreviation_map = json.load(f)

def preprocess_text(text):
    for abbr, full in abbreviation_map.items():
        pattern = r'\b' + re.escape(abbr) + r'\b'
        text = re.sub(pattern, full, text, flags=re.IGNORECASE)
    return text
