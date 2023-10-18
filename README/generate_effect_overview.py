import os

def generate_effect_overview(directory):
    content = "# Effect Overview\n\n"

    # Traverse the directory for .glsl files
    for root, _, files in os.walk(directory):
        for file in sorted(files):
            if file.endswith(".glsl"):
                base_name = os.path.splitext(file)[0]  # Get the name without extension
                png_file = base_name + ".png"

                # If the corresponding .png file exists, add to content
                if png_file in files:
                    content += f"## {base_name}\n"
                    content += f"![{base_name}]({png_file})\n\n"

    # Write to the file
    with open(os.path.join(directory, 'effect_overview.md'), 'w') as file:
        file.write(content)

    print(f"File 'effect_overview.md' has been generated in {directory}!")

if __name__ == "__main__":
    directory = '../'  # Directory path relative to the __scripts__ folder
    generate_effect_overview(directory)
