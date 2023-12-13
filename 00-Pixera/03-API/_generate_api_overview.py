import os
import re
import json

readme_prefix = """
# Protocol Overview
This documentation describes revision 367 of the API.

The Pixera API uses the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) protocol.

## Protocols

 - JSON/TCP
   - Requires header with prefix and message size
     - 'pxr1' + 4-byte size (least significant byte first)
       - `pxr1R000{{"jsonrpc": "2.0","id": 1,"method": "Pixera.Utility.getApiRevision"}}`
 - JSON/TDP(dl)
   - Requires delimiter
     - 0xPX
       - `{"jsonrpc": "2.0","id": 1,"method": "Pixera.Utility.getApiRevision"}0xPX`

# API Overview
"""


def read_api_json(version_directory):
    files = os.listdir(version_directory)
    if 'pixera_api.json' not in files:
        return
    else:
        print(f"Reading JSON file from {version_directory}")

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

def api_table(api_data):
    DEBUG_LIMIT = 9999
    debug_counter = 0
    output_lines = []  # Start with a header for the document

    def format_params(params, is_class_method=False):
        """Helper function to format parameters into a Markdown table cell."""
        formatted_params = []
        if is_class_method:
            formatted_params.append("`handle` : object<br>")  # Adding default `handle` parameter for class methods

        formatted_params.extend(f"`{p['name']}` : {p.get('type')} <br>" for p in params)
        return ''.join(formatted_params) if formatted_params else "None"

    def format_returns(returns):
        """Helper function to format return values into a Markdown table cell."""
        return ', '.join(f"`{r['name']}`<br>" for r in returns) if returns else "None"

    # Iterate over each namespace
    for namespace_name, namespace_info in api_data.items():
        if debug_counter >= DEBUG_LIMIT:
            break
        
        # Add a subsection for the namespace
        output_lines.append(f"## {namespace_name}\n")
        output_lines.append(f"Syntax: *Pixera.{namespace_name}.(function)*\n")

        # Section for functions
        if 'functions' in namespace_info:
            output_lines.append("### Functions\n")
            output_lines.append("| Name | Parameters | Return Values |\n")
            output_lines.append("| --- | --- | --- |\n")  # Table column format
            for function_name, function_info in namespace_info['functions'].items():
                if debug_counter >= DEBUG_LIMIT:
                    break
                params = format_params(function_info.get('params', []))
                returns = format_returns(function_info.get('returnValues', []))
                output_lines.append(f"| `{function_name}` | {params} | {returns} |\n")
                debug_counter += 1

        # Section for classes
        if namespace_info.get('classes'):  # Only show "Classes" if there are classes
            output_lines.append("### Classes\n")
            for class_name, class_info in namespace_info['classes'].items():
                if debug_counter >= DEBUG_LIMIT:
                    break
                output_lines.append(f"#### {class_name}\n")
                output_lines.append(f"Syntax: *Pixera.{namespace_name}.{class_name}.(method)*\n")
                output_lines.append("| Class Name | Method Name | Parameters | Return Values |\n")
                output_lines.append("| --- | --- | --- | --- |\n")
                debug_counter += 1
                
                if 'methods' in class_info:
                    for method_name, method_info in class_info['methods'].items():
                        if debug_counter >= DEBUG_LIMIT:
                            break
                        params = format_params(method_info.get('params', []), is_class_method=True)
                        returns = format_returns(method_info.get('returnValues', []))
                        output_lines.append(f"| `{class_name}` | `{method_name}` | {params} | {returns} |\n")
                        debug_counter += 1
        
        # Add space between namespaces
        output_lines.append("\n")

    return ''.join(output_lines)  # Join all lines into a single string separated by newlines





def generate_api_overview(api_data, output_path):
    overview_content = api_table(api_data)
    with open(output_path, 'w') as md_file:
        md_file.write(readme_prefix)
        md_file.write(overview_content)

def create_dictionary(json_data):

    if not json_data:  # Check if json_data is None or empty
        return
    
    # RECURSIVE NAMESPACE FUNCTION
    def process_namespace(namespace):
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
    
    # Initialize an empty dictionary to hold the organized data
    organized_json_data = {}

    # Loop through each namespace in the JSON data
    for namespace in json_data["namespaces"]:
        namespace_name = namespace["name"]
        
        # Initialize dictionaries for the namespace if they don't exist
        organized_json_data[namespace_name] = {
            'functions': {},
            'classes': {},
            'namespaces': {}
        }

        process_namespace(namespace)

        # Catch Settings and Unreal namespaces
        if 'namespaces' in namespace:
            for name in namespace["namespaces"]:
                process_namespace(name)

    return organized_json_data


if __name__ == "__main__":
    print("Generating API Overview")
    version_directory = './'
    json_data = read_api_json(version_directory)
    data = create_dictionary(json_data)
    generate_api_overview(data, "_api_overview.md")
    print("API Overview generated successfully.")
