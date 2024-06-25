import argparse
import json
import yaml
import xml.etree.ElementTree as Etree
#task1
def parse_arguments():
    parser = argparse.ArgumentParser(description='Narzędzie do konwersji danych')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()