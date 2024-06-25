def load_xml(file_path):    #task6
    try:
        tree = Etree.parse(file_path)
        root = tree.getroot()
        return root
    except Etree.ParseError as e:
        print(f"Błąd podczas odczytu pliku XML: {e}")
        return None