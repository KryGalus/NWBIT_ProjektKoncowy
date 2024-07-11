import sys
import json
import xmltodict
import yaml
import xml.etree.ElementTree as ET

def convert_dict_to_xml(data_dict):
    """Converts a dictionary to XML format"""
    root = ET.Element("root")
    def build_tree(parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(parent, key)
                build_tree(child, value)
        elif isinstance(data, list):
            for item in data:
                item_element = ET.SubElement(parent, "item")
                build_tree(item_element, item)
        else:
            parent.text = str(data)

    build_tree(root, data_dict)
    return ET.ElementTree(root)

def main(input_file, output_file):
    # Load data from the input file
    try:
        with open(input_file, 'r') as f:
            content = f.read().strip()
            if not content:
                print("Input file is empty.")
                return

            if input_file.endswith('.json'):
                data = json.loads(content)
            elif input_file.endswith('.xml'):
                data = xmltodict.parse(content)
            elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
                data = yaml.safe_load(content)
            else:
                print("Unsupported input file format.")
                return
    except Exception as e:
        print(f"Error loading input file: {e}")
        return

    # Convert and save data to the output file
    try:
        with open(output_file, 'w') as f:
            if output_file.endswith('.json'):
                json.dump(data, f, indent=4)
            elif output_file.endswith('.xml'):
                tree = convert_dict_to_xml(data)
                tree.write(f)
            elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
                yaml.dump(data, f, default_flow_style=False)
            else:
                print("Unsupported output file format.")
                return
    except Exception as e:
        print(f"Error saving output file: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: data_converter.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)