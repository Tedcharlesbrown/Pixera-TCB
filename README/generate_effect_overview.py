import os

def generate_effect_overview(directory):
    content = "# Effect Overview\n\n"

    # Traverse the directory for .glsl files
    for root, _, files in os.walk(directory):
        for file in sorted(files):
            if file.endswith(".glsl"):
                base_name = os.path.splitext(file)[0]  # Get the name without extension
                glsl_path = os.path.join(root, file)
                png_path = os.path.join(root, base_name + ".png")

                # If the corresponding .png file exists, add to content
                if os.path.exists(png_path):
                    content += f"## {base_name}\n"
                    content += f"![{base_name}]({png_path})\n\n"

    # Write to the file
    with open('effect_overview.md', 'w') as file:
        file.write(content)

    print("File 'effect_overview.md' has been generated!")

if __name__ == "__main__":
    directory = "../Pixera/Shaders/v1.9.149"  # Replace with your directory path
    generate_effect_overview(directory)
