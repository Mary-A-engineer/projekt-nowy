def save_json(data, file_path):      #task3
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)