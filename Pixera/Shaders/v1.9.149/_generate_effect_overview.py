import os
import re

image_size = 500

def rename_png_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png') and not file.endswith('.png'):
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, file[:-4] + '.png')
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")


def extract_labels(file_path):
    labels = []

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'//@ label: "(.+?)"', line)
            if match:
                labels.append(f'`{match.group(1)}`')  # Wrap each label in `

    return '\n'.join(labels)  # Return labels separated by new lines

def generate_effect_overview(directory):
    content = "# Effect Overview\n\n"
    placeholder_img = "_noeffect.png"  # Placeholder image filename

    # Traverse the directory for .glsl files
    for root, _, files in os.walk(directory):
        # Convert filenames to lowercase for case-insensitive comparison
        files_lower = [f.lower() for f in files]

        for file in sorted(files):
            if file.lower().endswith(".glsl"):
                base_name = os.path.splitext(file)[0]  # Get the name without extension
                png_file = base_name + ".png"
                
                label_str = extract_labels(os.path.join(root, file))

                if png_file.lower() in files_lower:
                    content += f"## {base_name}\n"
                    content += f'<img src="{png_file}" alt="{base_name}" width="{image_size}"/>\n\n'
                    content += f"**Labels:**\n\n{label_str}\n"  # Each label on a new line
                else:
                    content += f"## {base_name}\n"
                    content += f'<img src="{placeholder_img}" alt="Placeholder Image" width="{image_size}"/>\n\n'
                    content += f"**Labels:**\n\n{label_str}\n"

    # Use an absolute path to ensure the file is written to the correct directory
    output_path = os.path.abspath(os.path.join(directory, '_effect_overview.md'))
    with open(output_path, 'w') as file:
        file.write(content)

    print(f"File 'effect_overview.md' has been generated at {output_path}!")

if __name__ == "__main__":
    directory = './'  # Directory path relative to the __scripts__ folder
    rename_png_files(directory)
    generate_effect_overview(directory)
