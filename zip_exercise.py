import zipfile
import shutil
import os

# Functions to implement:
# create_zip(zip_path, files)

# Create a zip archive at zip_path containing the given list of file paths.
# list_contents(zip_path)

# Return a list of filenames inside the zip, along with their compressed and uncompressed sizes.
# extract_file(zip_path, filename, dest_dir)
# Extract a single file by name from the zip to dest_dir.

# search_in_zip(zip_path, keyword)
# Without fully extracting, read each text file inside the zip and return a list of filenames that contain the keyword.

# merge_zips(zip_paths, output_path)
# Merge multiple zip files into a single one, avoiding duplicate filenames (keep the first occurrence).

# Bonus (advanced):
# zip_from_dict(zip_path, data)
# Create a zip where each key in data is a filename and its value is the file's text content — without writing any files to disk first.


files_to_zip = [
    os.path.join("zip_folder", f)
    for f in os.listdir("zip_folder")
    if os.path.isfile(os.path.join("zip_folder", f))
]


def create_zip(zip_path, files):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, arcname=os.path.basename(file))


def list_zip_files(file):
    with zipfile.ZipFile(file, "r") as zip_ref:
        files_list = zip_ref.namelist()
        print(f"files in {file} are: {files_list}")


def info_zip_file(file):
    with zipfile.ZipFile(file, "r") as zip_ref:
        files_info = zip_ref.infolist()
        for info in files_info:
            print(f"File: {info.filename}")
            print(f" Modified: {info.date_time}")
            print(f" Size (uncompressed): {info.file_size} bytes")
            print(f" Size (compressed): {info.compress_size} bytes")


def extract_file(zip_path, filename, dest_dir):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        if filename in zip_ref.namelist():
            zip_ref.extract(filename, path=dest_dir)
        else:
            print(f"File {filename} doesn't exist in {zip_path}")


def search_in_zip(zip_path, keyword):
    # Get list of files
    result_list = []
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        for file in zip_ref.namelist():
            with zip_ref.open(file, "r") as handle_file:
                for line in handle_file:
                    if keyword in line.decode("utf-8").strip():
                        result_list.append(file)
                        break

    print(f"Files in {zip_path} that contains {keyword} are {result_list}")
    return result_list


create_zip("output.zip", files_to_zip)
list_zip_files("output.zip")
info_zip_file("output.zip")
extract_file("output.zip", "test.txt", "dest_dir")
search_in_zip("output.zip", "t")
