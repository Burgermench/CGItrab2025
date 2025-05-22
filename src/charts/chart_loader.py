import json

def load_chart(path="charts/note_chart.json"):
    with open(path, "r") as f:
        return json.load(f)