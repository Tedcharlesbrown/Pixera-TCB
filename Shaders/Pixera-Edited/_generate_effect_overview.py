import os
import re
import csv

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
                labels.append(f'`{match.group(1)}`')

    return '\n'.join(labels)

def get_shader_descriptions(directory):
    descriptions = {}
    csv_path = os.path.join(directory, 'description.csv')
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            shader = row['shader']
            description = row['description']
            notes = row['notes']
            descriptions[shader] = (description, notes)
    return descriptions

def generate_effect_overview(version_directory, description_directory):
    content = "# Effect Overview\n\n"
    placeholder_img = "_noeffect.png"

    shader_descriptions = get_shader_descriptions(description_directory)

    for root, _, files in os.walk(version_directory):
        files_lower = [f.lower() for f in files]

        for file in sorted(files):
            if file.lower().endswith(".glsl") and file.lower() != "blank.glsl":
                base_name = os.path.splitext(file)[0]
                png_file = base_name + ".png"

                label_str = extract_labels(os.path.join(root, file))

                content += f"## [{base_name}]({file})\n"
                
                if png_file.lower() in files_lower:
                    content += f'<img src="{png_file}" alt="{base_name}" width="{image_size}"/>\n\n'
                else:
                    content += f'<img src="{placeholder_img}" alt="Placeholder Image" width="{image_size}"/>\n\n'

                # Add description and notes from the CSV
                if base_name in shader_descriptions:
                    description, notes = shader_descriptions[base_name]
                    content += f"- {description}\n\n"
                    content += f"> {notes}\n\n"

                content += f"**Variables:**\n\n{label_str}\n"

    output_path = os.path.abspath(os.path.join(version_directory, '_effect_overview.md'))
    with open(output_path, 'w') as file:
        file.write(content)

    print(f"File 'effect_overview.md' has been generated at {output_path}!")

if __name__ == "__main__":
    version_directory = './'
    description_directory = '../'
    rename_png_files(version_directory)
    generate_effect_overview(version_directory, description_directory)
