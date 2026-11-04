from pathlib import Path
import json


TEAMS = Path(__file__).parent / "data" / "teams.json"
MATCHES = Path(__file__).parent / "data" / "matches.json"

def write_to_file(file_path, content):
    with open(file_path, "w", encoding="utf-8"):
        json.dump(content, file_path, indent=2)


def get_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as content:
            return json.load(content)


