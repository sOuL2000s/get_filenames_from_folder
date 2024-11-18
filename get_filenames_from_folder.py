import os

def get_filenames_from_folder(folder_path):
    try:
        filenames = os.listdir(folder_path)  # Get all filenames in the folder
        full_paths = [os.path.join(folder_path, f) for f in filenames]  # Get full file paths
        print("Files in the folder:")
        for file in full_paths:
            print(file)  # Print each filename
        return full_paths
    except FileNotFoundError:
        print("The folder does not exist. Please check the path.")
        return []

# Example usage:
folder = "D:\Movies\pov"  # Replace with your folder path
files = get_filenames_from_folder(folder)
