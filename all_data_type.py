import os
import json

def print_and_save_schema(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    
    output_file_path = os.path.splitext(json_file_path)[0] + '_schema.txt'

    with open(output_file_path, 'w') as output_file:
        print_data_type(data, output_file)

def print_data_type(data, output_file, indent=""):
    if isinstance(data, dict):
        for key, value in data.items():
            output_file.write(f"{indent}{key}: {type(value).__name__}\n")
            print(f"{indent}{key}: {type(value).__name__}")
            if isinstance(value, dict):
                print_data_type(value, output_file, indent + "    ")
            elif isinstance(value, list) and value:
                if isinstance(value[0], dict):
                    print_data_type(value[0], output_file, indent + "    ")
                elif isinstance(value[0], list):
                    print_data_type(value[0], output_file, indent + "    ")
                    output_file.write(f"{indent}{key}: list\n")
                    print(f"{indent}{key}: list")
                    for index, item in enumerate(value):
                        output_file.write(f"{indent}  [{index}]: {item} {type(item).__name__}\n")
                        print(f"{indent}  [{index}]: {type(item).__name__}")
    else:
        output_file.write(f"{indent}{type(data).__name__}\n")
        print(f"{indent}{type(data).__name__}")

folder_path = input('Name of the folder to scan')

json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

for json_file in json_files:
    json_file_path = os.path.join(folder_path, json_file)
    print_and_save_schema(json_file_path)

