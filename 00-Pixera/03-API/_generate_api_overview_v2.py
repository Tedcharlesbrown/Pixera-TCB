import os
import re
import json


def read_api_json(version_directory):
    files = os.listdir(version_directory)
    if 'pixera_api.json' not in files:
        return
    else:
        print("FOUND FILE")

    file_path = os.path.join(version_directory, "pixera_api.json")
    with open(file_path, 'r', encoding='utf-8-sig') as f:  # Use 'utf-8-sig' encoding
            content = f.read().strip()  # Read and strip the content
            try:
                data = json.loads(content)  # Parse the stripped content
                return data
            except json.JSONDecodeError as e:
                print(f"Error: The file {file_path} is not a valid JSON file or is empty.")
                print(f"Error details: {e}")  # Print the error details
                return
            
# ---------------------------------------------------------------------------- #
#                                   OPTION 1                                   #
# ---------------------------------------------------------------------------- #

def api_list(api_data):
    DEBUG_LIMIT = 9999
    debug_counter = 0
    output_lines = []  # Initialize a list to collect output lines

    # Iterate over each namespace
    for namespace_name, namespace_info in api_data.items():
        if debug_counter >= DEBUG_LIMIT:
            break
        output_lines.append(f"# {namespace_name}\n")
        
        # Check and print functions in the namespace
        functions = namespace_info.get('functions')
        if functions:
            output_lines.append("## Functions\n")
            for function_name, function_info in functions.items():
                if debug_counter >= DEBUG_LIMIT:
                    break
                output_lines.append(f"### `{function_name}`\n")
                output_lines.extend(print_params_and_return_values(function_info))
                debug_counter += 1
                
        # Check and print classes and their methods in the namespace
        classes = namespace_info.get('classes')
        if classes:
            output_lines.append("## Classes\n")
            for class_name, class_info in classes.items():
                if debug_counter >= DEBUG_LIMIT:
                    break
                output_lines.append(f"### {class_name}\n")
                
                # Check and print methods of the class
                methods = class_info.get('methods')
                if methods:
                    output_lines.append("#### Methods\n")
                    for method_name, method_info in methods.items():
                        if debug_counter >= DEBUG_LIMIT:
                            break
                        output_lines.append(f"##### `{method_name}`\n")
                        output_lines.extend(print_params_and_return_values(method_info))
                        debug_counter += 1
    
    # output_lines.append("---\n\n")  # Horizontal line after each namespace
    return '\n'.join(output_lines)  # Join all lines into a single string separated by newlines

def print_params_and_return_values(info):
    lines = []
    # Check and print parameters
    params = info.get('params')
    if params:
        lines.append("- **Parameters**\n\n")
        for param in params:
            lines.append(f"  - `{param['name']}` : {param.get('type', 'No Type Provided')}")
        lines.append("\n")
            
    # Check and print return values
    return_values = info.get('returnValues')
    if return_values:
        lines.append("- **Return Values**\n\n")
        for return_val in return_values:
            lines.append(f"  - `{return_val['name']}` : {return_val.get('type', 'No Type Provided')}")
        lines.append("\n")
    
    lines.append("---\n\n")  # Horizontal line after each function or method
    return lines  # Return the list of lines for this section

# ---------------------------------------------------------------------------- #
#                                   option 2                                   #
# ---------------------------------------------------------------------------- #

def api_table(api_data):
    DEBUG_LIMIT = 9999
    debug_counter = 0
    output_lines = ["# API Overview\n\n"]  # Start with a header for the document

    # Table headers
    output_lines.append("| Namespace | Entity | Type | Name | Parameters | Return Values |\n")
    output_lines.append("| --- | --- | --- | --- | --- | --- |\n")  # Table column format

    # Iterate over each namespace
    for namespace_name, namespace_info in api_data.items():
        if debug_counter >= DEBUG_LIMIT:
            break
        
        # If there are functions or classes in the namespace, iterate through them
        if 'functions' in namespace_info or 'classes' in namespace_info:
            if 'functions' in namespace_info:
                for function_name, function_info in namespace_info['functions'].items():
                    if debug_counter >= DEBUG_LIMIT:
                        break
                    params = format_params(function_info.get('params', []))
                    returns = format_returns(function_info.get('returnValues', []))
                    output_lines.append(f"| {namespace_name} | Function | | `{function_name}` | {params} | {returns} |\n")
                    debug_counter += 1

            if 'classes' in namespace_info:
                for class_name, class_info in namespace_info['classes'].items():
                    if debug_counter >= DEBUG_LIMIT:
                        break
                    # Class row with no method details
                    output_lines.append(f"| {namespace_name} | Class | | `{class_name}` | | |\n")
                    debug_counter += 1
                    
                    if 'methods' in class_info:
                        for method_name, method_info in class_info['methods'].items():
                            if debug_counter >= DEBUG_LIMIT:
                                break
                            params = format_params(method_info.get('params', []))
                            returns = format_returns(method_info.get('returnValues', []))
                            output_lines.append(f"| | | Method | `{method_name}` | {params} | {returns} |\n")
                            debug_counter += 1
        else:
            # Namespace with no functions or classes
            output_lines.append(f"| {namespace_name} | | | | | |\n")

    return ''.join(output_lines)  # Join all lines into a single string separated by newlines


def format_params(params):
    """Helper function to format parameters into a Markdown table cell."""
    if not params:
        return "None"
    return ', '.join(f"`{p['name']}`: {p.get('type', 'No Type Provided')}" for p in params)

def format_returns(returns):
    """Helper function to format return values into a Markdown table cell."""
    if not returns:
        return "None"
    return ', '.join(f"`{r['name']}`: {r.get('type', 'No Type Provided')}" for r in returns)



def generate_api_overview(api_data, output_path):
    overview_content = api_table(api_data)
    with open(output_path, 'w') as md_file:
        md_file.write(overview_content)

def create_dictionary(json_data):
    if not json_data:  # Check if json_data is None or empty
        return
    
    # Initialize an empty dictionary to hold the organized data
    organized_json_data = {}

    # Loop through each namespace in the JSON data
    for namespace in json_data["namespaces"]:
        namespace_name = namespace["name"]
        
        # Initialize dictionaries for the namespace if they don't exist
        organized_json_data[namespace_name] = {
            'functions': {},
            'classes': {}  # Initialize 'classes' dictionary here
        }

        # Check if the 'functions' key exists before proceeding
        if 'functions' in namespace:
            # Loop through each function in the current namespace
            for function in namespace["functions"]:
                function_name = function["name"]

                # Store the function with its params and return values
                organized_json_data[namespace_name]['functions'][function_name] = {
                    'params': function.get("params", []),  # Use .get() to avoid KeyError
                    'returnValues': function.get("returnValues", [])  # Use .get() to avoid KeyError
                }
        
            # Check if the 'classes' key exists before proceeding
            if 'classes' in namespace:
                # Loop through each class in the current namespace
                for class_ in namespace["classes"]:
                    class_name = class_["name"]

                    # Initialize dictionary for the class
                    organized_json_data[namespace_name]['classes'][class_name] = {
                        'methods': {},
                        # 'params': class_.get("params", [])  # Classes might not have params at this level, depending on your JSON structure
                    }
                    
                    # Check if the 'methods' key exists in the class before proceeding
                    if 'methods' in class_:
                        # Loop through each method in the current class
                        for method in class_["methods"]:
                            method_name = method["name"]

                            # Store the class method with its params and return values
                            organized_json_data[namespace_name]['classes'][class_name]['methods'][method_name] = {
                                'params': method.get("params", []),
                                'returnValues': method.get("returnValues", [])
                            }
    return organized_json_data

    # utility_functions = api_data.get('Utility', {}).get('functions', {})
    # get_api_revision_data = utility_functions.get('getApiRevision', {})



if __name__ == "__main__":
    version_directory = './'
    json_data = read_api_json(version_directory)
    data = create_dictionary(json_data)
    generate_api_overview(data, "_api_overview.md")
