import json

def save_data_to_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)