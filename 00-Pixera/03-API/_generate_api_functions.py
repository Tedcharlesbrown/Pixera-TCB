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
    processed_classes = set()  # Keep track of processed classes

    def process_namespace(namespace, namespace_name):
        if namespace_name not in organized_data:
            organized_data[namespace_name] = {'functions': {}, 'classes': {}}

        for function in namespace.get("functions", []):
            function_name = function["name"]
            organized_data[namespace_name]['functions'][function_name] = function

        for class_ in namespace.get("classes", []):
            class_name = class_["name"]
            # Check if the class has already been processed
            if class_name in processed_classes:
                continue
            processed_classes.add(class_name)
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
        s = s.replace("string", "str").replace("double", "float").replace("null", "None")
        if s.endswith("[]"):
            base_type = s[:-2]
            return f"List[{replace_types(base_type)}]"
        if s.startswith("optional<") and s.endswith(">"):
            base_type = s[9:-1]
            return f"Optional[{replace_types(base_type)}]"
        return s

    code_lines = [
        "from typing import Optional, List\n",
        "class uint:\n    pass\n\n",
        "class handle:\n    pass\n\n",
        "class ScreenPosValues:\n    pass\n\n",
        "class ProjectorPosValues:\n    pass\n\n",
        "class TimelineAttributes:\n    pass\n\n",
        "class timelineParamValue:\n    pass\n\n",
        "class TransportAttributes:\n    pass\n\n",
        "class CueAttributes:\n    pass\n\n",
        "class API:\n"
    ]

    processed_classes = set()

    for namespace_name, namespace_info in api_data.items():
        for function_name, function_info in namespace_info['functions'].items():
            all_params = ', '.join([f"{param['name']}: {replace_types(param['type'])}" for param in function_info.get('params', [])])
            param_names = [param['name'] for param in function_info.get('params', [])]
            return_values = ', '.join([replace_types(ret['type']) for ret in function_info.get('returnValues', [])])
            return_type = f" -> {return_values}" if return_values else ""
            params_list_string = '[' + ', '.join(f'"{name}"' for name in param_names) + ']' if param_names else '[]'
            params_list = '[' + ', '.join(param_names) + ']' if param_names else '[]'

            function_definition = (
                f"    @staticmethod\n"
                f"    def {function_name}({all_params}){return_type}:\n"
                f"        method = \"Pixera.{namespace_name}.{function_name}\"\n"
                f"        params = {params_list_string}\n"
                f"        return [method, params, {params_list}]\n\n"
            )
            code_lines.append(function_definition)

        for class_name, class_info in namespace_info['classes'].items():
            if class_name in processed_classes:
                continue
            processed_classes.add(class_name)
            class_definition = f"    class {class_name}:\n"
            for method_name, method_info in class_info['methods'].items():
                params_list = [f"{param['name']}: {replace_types(param['type'])}" for param in method_info.get('params', [])]
                handle_param = "handle: handle"
                if params_list:
                    handle_param += ", " + ', '.join(params_list)
                param_names_list = [param['name'] for param in method_info.get('params', [])]
                param_names_with_handle = "handle"
                if param_names_list:
                    param_names_with_handle += ", " + ', '.join(param_names_list)
                return_values = ', '.join([replace_types(ret['type']) for ret in method_info.get('returnValues', [])])
                return_type = f" -> {return_values}" if return_values else ""
                method_definition = (
                    f"        @staticmethod\n"
                    f"        def {method_name}({handle_param}){return_type}:\n"
                    f"            method = \"Pixera.{namespace_name}.{class_name}.{method_name}\"\n"
                    f"            params = [\"{param_names_with_handle}\"]\n\n"
                    f"            return [method, params, [{param_names_with_handle}]]\n\n"
                )
                class_definition += method_definition

            if not class_info['methods']:
                class_definition += "        pass\n\n"

            code_lines.append(class_definition)

    return ''.join(code_lines)



def main():
    version_directory = './'
    json_data = read_api_json(version_directory)
    if json_data:
        api_data = create_dictionary(json_data)
        if api_data:
            python_code = generate_python_code(api_data)
            with open('../../01-Custom/03-API/src/api/api_functions.py', 'w') as file:
                file.write(python_code)
            print("Python API file generated successfully.")
        else:
            print("Failed to organize JSON data.")
    else:
        print("Failed to read JSON file.")

if __name__ == "__main__":
    main()
