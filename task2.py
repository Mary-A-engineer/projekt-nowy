def load_json(file_path):  
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f"Błąd podczas odczytu pliku JSON: {e}")
        return None