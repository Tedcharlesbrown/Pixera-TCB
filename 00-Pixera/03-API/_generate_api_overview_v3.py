import os
import json

def read_api_json(version_directory):
    file_path = os.path.join(version_directory, "pixera_api.json")
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing the file: {e}")
        return None

def create_dictionary(json_data):
    if not json_data:
        return None

    organized_data = {}
    def process_namespace(namespace, namespace_name):
        organized_data[namespace_name] = {'functions': {}, 'classes': {}}
        for function in namespace.get("functions", []):
            function_name = function["name"]
            organized_data[namespace_name]['functions'][function_name] = function

        for class_ in namespace.get("classes", []):
            class_name = class_["name"]
            organized_data[namespace_name]['classes'][class_name] = {'methods': {}}
            for method in class_.get("methods", []):
                method_name = method["name"]
                organized_data[namespace_name]['classes'][class_name]['methods'][method_name] = method

        for nested_namespace in namespace.get("namespaces", []):
            process_namespace(nested_namespace, f"{namespace_name}.{nested_namespace['name']}")

    for namespace in json_data["namespaces"]:
        process_namespace(namespace, namespace["name"])

    return organized_data

def generate_python_code(api_data):
    def replace_types(s):
        return s.replace("string", "str").replace("double", "float").replace("null", "None")

    code_lines = []

    for namespace_name, namespace_info in api_data.items():
        for function_name, function_info in namespace_info['functions'].items():
            # Generate parameter list with types
            all_params = ', '.join([f"{param['name']}: {replace_types(param['type'])}" 
                                    for param in function_info.get('params', [])])

            # Generate simple parameter list without types
            params = ', '.join([f"{param['name']}" for param in function_info.get('params', [])])

            # Generate return types
            return_values = ', '.join([replace_types(ret['type']) 
                                       for ret in function_info.get('returnValues', [])])

            return_type = f" -> {return_values}" if return_values else ""
            full_function_name = f"{function_name}"
            param_names = ', '.join([param.split(':')[0] for param in params.split(', ')])

            # Consolidated function definition with multi-line string formatting
            function_definition = (
                f"def {full_function_name}({all_params}){return_type}:\n"
                f"    method = \"Pixera.{namespace_name}.{function_name}\"\n"
                f"    params = [\"{param_names}\"]\n\n"
                f"    return [method,params,[{param_names}]]\n\n"
            )
            code_lines.append(function_definition)

    # return ''.join(code_lines)



        for class_name, class_info in namespace_info['classes'].items():
            class_definition = f"class {class_name}:\n"
            for method_name, method_info in class_info['methods'].items():
                all_params = ', '.join([f"{param['name']}: {replace_types(param['type'])}" 
                                        for param in method_info.get('params', [])])
                params = ', '.join([f"{param['name']}" for param in method_info.get('params', [])])
                return_values = ', '.join([replace_types(ret['type']) 
                                           for ret in method_info.get('returnValues', [])])
                return_type = f" -> {return_values}" if return_values else ""
                param_names = ', '.join([param.split(':')[0] for param in params.split(', ')])

                method_definition = (
                    f"    def {method_name}({all_params}){return_type}:\n"
                    f"        method = \"Pixera.{namespace_name}.{class_name}.{method_name}\"\n"
                    f"        params = [\"{param_names}\"]\n\n"
                )
                class_definition += method_definition

            code_lines.append(class_definition)

    return ''.join(code_lines)


def main():
    version_directory = './'
    json_data = read_api_json(version_directory)
    if json_data:
        api_data = create_dictionary(json_data)
        if api_data:
            python_code = generate_python_code(api_data)
            with open('api_functions.py', 'w') as file:
                file.write(python_code)
            print("Python API file generated successfully.")
        else:
            print("Failed to organize JSON data.")
    else:
        print("Failed to read JSON file.")

if __name__ == "__main__":
    main()
