#deleting unneeded files
import os

def find_large_files(folder, size_limit_mb=100):
    size_limit = size_limit_mb * 1024 * 1024  # Convert MB to bytes

    print(f"Scanning '{folder}' for files larger than {size_limit_mb} MB...\n")

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            try:
                filepath = os.path.join(foldername, filename)
                filesize = os.path.getsize(filepath)
                if filesize > size_limit:
                    print(f"{os.path.abspath(filepath)} - {filesize / (1024 * 1024):.2f} MB")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Cannot access {filepath}: {e}")

# Example usage
if __name__ == "__main__":
    folder_to_search = input("Enter the path to the folder to scan: ")
    find_large_files(folder_to_search)
