def xml_to_dict(element):  #task7
    data = {}
    for child in element:
        if len(child):
            data[child.tag] = xml_to_dict(child)
        else:
            data[child.tag] = child.text
    return data

def dict_to_xml(data, root_tag='root'):
    root = Etree.Element(root_tag)
    _dict_to_xml_recurse(data, root)
    return root

def _dict_to_xml_recurse(data, parent):
    for key, value in data.items():
        if isinstance(value, dict):
            child = Etree.SubElement(parent, key)
            _dict_to_xml_recurse(value, child)
        else:
            child = Etree.SubElement(parent, key)
            if value is not None:
                child.text = str(value)

def save_xml(data, file_path):
    tree = Etree.ElementTree(data)
    tree.write(file_path)

if name == "main":
    args = parse_arguments()
    
    data = None

    if args.input_file.endswith('.json'):
        data = load_json(args.input_file)
    elif args.input_file.endswith('.yaml') or args.input_file.endswith('.yml'):
        data = load_yaml(args.input_file)
    elif args.input_file.endswith('.xml'):
        data = load_xml(args.input_file)
        if data is not None:
            data = xml_to_dict(data)
    else:
        print("Nieobsługiwany format pliku wejściowego")

    if data is not None:
        if args.output_file.endswith('.json'):
            save_json(data, args.output_file)
        elif args.output_file.endswith('.yaml') or args.output_file.endswith('.yml'):
            save_yaml(data, args.output_file)
        elif args.output_file.endswith('.xml'):
            xml_data = dict_to_xml(data)
            save_xml(xml_data, args.output_file)
        else:
            print("Nieobsługiwany format pliku wyjściowego")
    else:
        print("Nieudało się załadować pliku wejściowego")