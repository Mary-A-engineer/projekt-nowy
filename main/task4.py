def load_yaml(file_path):  #task4
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except yaml.YAMLError as e:
        print(f"Błąd podczas odczytu pliku YAML: {e}")
        return None