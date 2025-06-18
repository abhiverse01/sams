import os


def generate_tree(
    directory, prefix="", level=0, max_level=4, exclude=None, output_file=None
):
    if exclude is None:
        exclude = [
            "senv",
            "env",
            "venv",
            ".venv",
            "__pycache__",
            ".git",
            "node_modules",
        ]  # Directories to exclude before creating project structure

    if level > max_level:
        return

    files = []
    folders = []
    for item in os.listdir(directory):
        if item in exclude:
            continue
        if os.path.isfile(os.path.join(directory, item)):
            files.append(item)
        else:
            folders.append(item)

    for folder in sorted(folders):
        line = f"{prefix}├── {folder}/\n"
        if output_file:
            output_file.write(line)
        print(line, end="")
        generate_tree(
            os.path.join(directory, folder),
            prefix + "│   ",
            level + 1,
            max_level,
            exclude,
            output_file,
        )

    for file in sorted(files):
        line = f"{prefix}└── {file}\n"
        if output_file:
            output_file.write(line)
        print(line, end="")


# Usage:
root_dir = "."  # Use the current directory
output_filename = "project_stx.txt"

# Open the file with utf-8 encoding
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(os.path.basename(os.getcwd()) + "/\n")
    generate_tree(root_dir, output_file=f)

print(f"\nTree structure saved to {output_filename}")
