import zipfile


def count_zipped_files(zip_path: str) -> int:
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        return len([_ for _ in zip_file.infolist() if not _.is_dir()])


# Finds the full path of the largest file within a zip. In case of ties, it uses lexicographical order
def largest_file_in_zip(zip_path: str) -> str:
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        file_infos = [
            file_info for file_info in zip_file.infolist() if not file_info.is_dir()
        ]
        if not file_infos:
            return None
        sorted_files = sorted(file_infos, key=lambda f: (-f.file_size, f.filename))
        return sorted_files[0].filename


# Retrieves the contents of the largest file in a zip, with tie-breaking as in the prior function
def largerst_zipped_file_contents(zip_path: str) -> str:
    largest_file = largest_file_in_zip(zip_path)
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        return zip_file.read(largest_file).decode("utf-8")


count = count_zipped_files("output.zip")
print(count)
largest_file = largest_file_in_zip("output.zip")
print(largest_file)
contents = largerst_zipped_file_contents("output.zip")
print(contents)
