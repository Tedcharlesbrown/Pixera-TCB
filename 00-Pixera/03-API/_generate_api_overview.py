import os
import re
import json

readme_prefix = """
# Protocol Overview
This documentation describes revision 349 of the API.

The Pixera API uses the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) protocol.

Pixera API test application by Benni Müller can be found [here](http://www.benni-m.de/index.html#projects).

Descriptions pulled from [pixera_api_examples_rev349.txt](00-Pixera/03-API/docs/pixera_api_examples_rev349.txt)

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



# def build_function_descriptions(file_path):
#     # Read the content of the other file
#     with open(file_path, 'r') as f:
#         lines = f.readlines()

#     comments = []
#     for line in lines:
#         stripped_line = line.strip()
#         if stripped_line.startswith("//"):
#             # Collect comment lines
#             comments.append(stripped_line.replace('//', '- '))
#         elif '(' in stripped_line and ');' in stripped_line:
#             function_name = stripped_line.split('(')[0].split()[-1]
#             function_descriptions[function_name] = "\n".join(comments) + "\n\n"
#             comments = []  # Reset comments for the next function

def build_function_descriptions(file_path):
    # Read the content of the other file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Define the start and end markers of the block to ignore
    start_marker = "// The Compound namespace contains functions that represent core Pixera capabilites and can be invoked"
    end_marker = "namespace Compound"

    # Flag to determine if we are inside the block to ignore
    ignore_block = False

    comments = []
    for line in lines:
        stripped_line = line.strip()

        # Check if we are entering or leaving the block to ignore
        if stripped_line == start_marker:
            ignore_block = True
        elif stripped_line == end_marker:
            ignore_block = False
            comments = []  # Reset comments after the end marker
            continue  # Skip the current line and move to the next

        # If we are inside the block to ignore, skip processing
        if ignore_block:
            continue

        if stripped_line.startswith("//"):
            # Collect comment lines
            comments.append(stripped_line.replace('//', '- '))
        elif '(' in stripped_line and ');' in stripped_line:
            # This is a simplistic check for a function line
            function_name = stripped_line.split('(')[0].split()[-1]
            function_descriptions[function_name] = "\n".join(comments) + "\n\n"
            comments = []  # Reset comments


def get_function_description(function_name):
    return function_descriptions.get(function_name, "")

def generate_api_overview(json_data):
    example_json = """
    => {"jsonrpc":"2.0", "id":3, "method":"Pixera.Utility.outputDebug", "params":{"message":"Hello World"}}
    <= {"jsonrpc":"2.0", "id":3, "result":"Hello World"}
    """


    if not json_data:  # Check if json_data is None or empty
        return

    output_path = '_api_overview.md'
    with open(output_path, 'w') as f:
        f.write(readme_prefix)
        f.write(f"## {json_data['name']}\n\n")
        # f.write("---\n\n")  # Horizontal line


        # Loop through namespaces
        for namespace in json_data['namespaces']:
            # Write namespace name as a subsection
            f.write(f"### {namespace['name']}\n\n")
            # f.write("---\n\n")  # Horizontal line

            # Loop through functions in each namespace
            if 'functions' in namespace:
                for function in namespace['functions']:
                    formatted_function_name = re.sub(r'(?<=[a-z])([A-Z])', r' \1', function['name']).strip().upper()
                    f.write(f"**{formatted_function_name}**\n")
                    f.write(f"\n`{json_data['name']}.{namespace['name']}.{function['name']}`\n\n")

                    # If there is a description, write it
                    f.write(get_function_description(function['name']))
                    # return

                    # If there are parameters, list them
                    if function['params']:
                        f.write("   - **Parameters**:\n")
                        for param in function['params']:
                            f.write(f"     - `{param['name']}` : *{param['type']}*\n")
                        f.write("\n")

                    # If there are return values, list them
                    if function['returnValues']:
                        f.write("   - **Return Values**:\n")
                        for ret_val in function['returnValues']:
                            f.write(f"     - `{ret_val['name']}` : *{ret_val['type']}*\n")
                        f.write("\n")

                    f.write("---\n\n")  # Horizontal line after each function


# Dictionary to store function descriptions
function_descriptions = {}

if __name__ == "__main__":
    version_directory = './'
    build_function_descriptions("docs/pixera_api_examples_rev349.txt")
    json_data = read_api_json(version_directory)
    generate_api_overview(json_data)
