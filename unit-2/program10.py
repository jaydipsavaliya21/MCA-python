import zipfile
import os


def zip_files(file_list, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_list:
            if os.path.exists(file):
                zipf.write(file)
                print(f"Added {file} to {zip_name}")
            else:
                print(f"File {file} not found!")

def unzip_files(zip_name, extract_path):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_path)
        print(f"Extracted all files to {extract_path}")


if __name__ == "__main__":
    # List of files to zip
    files_to_zip = ["source.txt", "marks.txt", "numbers.txt"]  # replace with your files
    zip_filename = "my_archive.zip"

    # Zip the files
    zip_files(files_to_zip, zip_filename)

    # Unzip the files
    unzip_files(zip_filename, "extracted_files")
