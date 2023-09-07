import os

def generate_directory_tree(start_path, excluded_dirs=[], output_file="directory_tree.txt"):
    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(start_path):
            # Exclude specified directories
            dirs[:] = [d for d in dirs if d not in excluded_dirs]

            # Indentation based on the depth of the directory
            depth = root.replace(start_path, '').count(os.sep)
            indent = ' ' * 4 * depth

            # Write the directory path to the output file
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))

            # Write the filenames in the current directory
            subindent = ' ' * 4 * (depth + 1)
            for file in files:
                f.write('{}{}\n'.format(subindent, file))

# Example usage
start_directory = os.path.dirname(os.path.abspath(__file__))
excluded_directories = ['__pycache__', '.devcontainer', 'migrations', 'data', 'pgadmin']  # Replace with your excluded directories
generate_directory_tree(start_directory, excluded_directories)
