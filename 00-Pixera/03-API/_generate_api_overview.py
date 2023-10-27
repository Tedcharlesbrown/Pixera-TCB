import os
import re
import json

readme_prefix = """
# Protocol Overview

The Pixera API uses the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) protocol.

Pixera API test application by Benni Müller can be found [here](http://www.benni-m.de/index.html#projects).

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

def generate_api_overview(json_data):
    if not json_data:  # Check if json_data is None or empty
        return

    output_path = '_api_overview.md'
    with open(output_path, 'w') as f:
        # Write the main name as a title
        f.write(f"# {json_data['name']}\n\n")

        # Loop through namespaces
        for namespace in json_data['namespaces']:
            # Write namespace name as a subsection
            f.write(f"## {namespace['name']}\n\n")

            # Loop through functions in each namespace
            if 'functions' in namespace:
                for function in namespace['functions']:

                    # Write function name as a subsection
                    f.write(f"### {function['name']}\n")
                    f.write(f"`{json_data['name']}.{namespace['name']}.{function['name']}`\n")

                    # If there are parameters, list them
                    if function['params']:
                        f.write("- **Sending Parameters**:\n")
                        for param in function['params']:
                            f.write(f"  -  `{param['name']}` : *{param['type']}*\n")
                        f.write("\n")

                    # If there are return values, list them
                    if function['returnValues']:
                        f.write("- **Return Values**:\n")
                        for ret_val in function['returnValues']:
                            f.write(f"  -  `{ret_val['name']}` : *{ret_val['type']}*\n")
                        f.write("\n\n")

def generate_api_overview_1(json_data):
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

                    # If there are parameters, list them
                    if function['params']:
                        f.write("- **Parameters**:\n")
                        for param in function['params']:
                            f.write(f"  - `{param['name']}` : *{param['type']}*\n")
                        f.write("\n")

                    # If there are return values, list them
                    if function['returnValues']:
                        f.write("- **Return Values**:\n")
                        for ret_val in function['returnValues']:
                            f.write(f"  - `{ret_val['name']}` : *{ret_val['type']}*\n")
                        f.write("\n")

                    f.write("---\n\n")  # Horizontal line after each function


if __name__ == "__main__":
    version_directory = './'
    json_data = read_api_json(version_directory)
    generate_api_overview_1(json_data)


    # for file in files:
    #     if file.find("pixera_api.json"):
    #         print(file)
    #         with open(file, 'r') as f:
    #             print(f.read())

    # print(files)


    # output_path = os.path.abspath(os.path.join(version_directory, '_api_overview.md'))
    # with open(output_path, 'w') as file:
    #     file.write("TEST")

    # print(f"File '_api_overview.md' has been generated at {output_path}!")