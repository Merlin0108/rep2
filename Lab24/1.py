import os

def list_files_by_extension(directory, extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError("Directory not found")

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    print(os.path.join(root, file))

    except FileNotFoundError as e:
        print(f"Error: {e}")

directory = input("Enter the path to the directory: ")
extension = input("Enter the file extension to filter by (txt,tht,png,tt,jpg): ")

list_files_by_extension(directory, extension)