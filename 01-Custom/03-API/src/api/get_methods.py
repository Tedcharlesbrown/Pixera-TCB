def get_methods(file_path):
    """
    Parses a file to extract the formatted strings and converts them into a specified format.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    methods = []
    for line in lines:
        if line.startswith('`'):
            method_name = line.strip().strip('`')
            methods.append(method_name)

    # Convert to the desired format
    formatted_strings = []
    for method in methods:
        # Convert camel case to uppercase with underscores
        formatted_name = ''.join(['_' + i if i.isupper() else i for i in method.split(".")[-1]]).lstrip('_').upper()
        formatted_string = f'{formatted_name} = "{method}"'
        formatted_strings.append(formatted_string)

    return formatted_strings

if __name__ == "__main__":
    file_path = r"../../../../00-Pixera/03-API/_api_overview.md"
    
    output_file = "methods.py"  # Replace with desired output file's path
    
    results = get_methods(file_path)
    
    with open(output_file, 'w') as f:
        f.write("class Methods:\n")
        for line in results:
            f.write(f"    {line}\n")