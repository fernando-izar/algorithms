import zipfile


# This function should return the number of files (not directories) in a zip archive
def count_zipped_files(zip_path: str) -> int:
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        return sum(1 for file_info in zip_file.infolist() if not file_info.is_dir())
        # counter = 0
        # for file_info in zip_file.infolist():
        #     if not file_info.is_dir():
        #         counter += 1
        # return counter


# Finds the full path of the largest file within a zip. In case of ties, it uses lexicographical order
def largest_file_in_zip(zip_path: str) -> str:
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        files = [
            file_info for file_info in zip_file.infolist() if not file_info.is_dir()
        ]
        # for f in files:
        #     print(f"File name: {f.filename}, size: {f.file_size}")
        sorted_files = sorted(files, key=lambda file: (-file.file_size, file.filename))
        # return sorted_files[0].filename
        # largest_file = max(files, key=lambda f: (f.file_size, f.filename))
        # return largest_file


# Retrieves the contents of the largest file in a zip, with tie-breaking as in the prior function
def largerst_zipped_file_contents(zip_path: str) -> str:
    file_name = largest_file_in_zip(zip_path)
    if not file_name:
        return ""
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        content_bytes = zip_file.read(file_name)
        content_str = content_bytes.decode("utf-8")
        return content_str


nr_zip_files = count_zipped_files("zipped_file")
# print(nr_zip_files)
largest_file_in_zip("zipped_file")

content = largerst_zipped_file_contents("output.zip")
print(f"Content is: {content}")


# names = ["axab", "abbb", "aaa"]

# sorted_names = sorted(names, key=lambda name: (len(name), name))
# largest_name = max(names, key=lambda name: (-len(name), name))
# print(largest_name)
