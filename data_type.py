import json
import random

def print_data_type(data, indent="", output_file=None):
    if output_file is None:
        output_file = open("schema_data_type.txt", "w")
    
    if isinstance(data, dict):
        for key, value in data.items():
            output_file.write(f"{indent}{key}: {type(value).__name__}\n")
            print(f"{indent}{key}: {type(value).__name__}")
            if isinstance(value, dict):
                print_data_type(value, indent + "    ", output_file)
            elif isinstance(value, list):
                print(indent+f"  -num of entries[{len(value)}]")
                if isinstance(value[0], dict):
                    print_data_type(value[0], indent + "    ", output_file)
                elif isinstance(value[0], list):
                    print_data_type(value[0], indent + "    ", output_file)
                    output_file.write(f"{indent}{key}: list\n")
                    print(f"{indent}{key}: list")
                    for index, item in enumerate(value):
                        output_file.write(f"{indent}  [{index}]: {item} {type(item).__name__}\n")
                        print(f"{indent}  [{index}]: {type(item).__name__}")
                        
          
    else:
        if type(data).__name__ is list:
            output_file.write(f"{indent}{type(data).__name__} [{len(data)}]\n")
            print(f"{indent}{type(data).__name__}  [{len(data)}]")
        else:
            output_file.write(f"{indent}{type(data).__name__}\n")
            print(f"{indent}{type(data).__name__}")

with open('Detalleequipo.json', 'r') as file:
    data = json.load(file)
    print_data_type(data)


        
        