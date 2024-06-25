def save_yaml(data, file_path):    #task5
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)