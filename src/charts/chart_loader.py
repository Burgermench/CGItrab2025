import json

def load_chart(path="chart/note_chart.json"):
    with open(path, "r") as f:
        return json.load(f)
    
# Load uma vez ou multiplas? Note: TODO: add remove?