import os

# Print the current directory
print(os.getcwd())


def find_git_folders(dir):
    """
    Find all git folders in the given directory
    """
    # Create a list to store all git folders
    git_folders = []

    # Loop through all files in the given directory
    for file in os.listdir(dir):
        file = os.path.join(dir, file)
        # Check if the file is a directory
        if os.path.isdir(file):
            # Check if the directory contains a .git folder
            if os.path.isdir(os.path.join(file, ".git")):
                # Add the directory to the list
                git_folders.append(file)
            # Recursively call the function to find all git folders in the subdirectories
            else:
                git_folders += find_git_folders(file)

    # Return the list of git folders
    return git_folders


folders = find_git_folders("C:\\dev")

for folder in folders:
    print(folder)
