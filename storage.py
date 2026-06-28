import json

FILE = "data.json"

# method to save data to a json file
def save(problems):
    data = [p.to_dict() for p in problems]
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# method to load data from a json file
def load():
    from problems import Problem
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
        return [Problem.from_dict(d) for d in data]
    except FileNotFoundError: # return empty list if json file does not exist
        return []
    
