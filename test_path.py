import os
import zipfile


file_paths = ["example1.txt", "example2.txt", "example3.txt"]
contents = ["content1 - Hello \n World!", "content2", "content3"]


for i in range(3):
    with open(file_paths[i], "w") as file:
        file.write(contents[i])

zip_file_path = "zip_exercises.zip"

with zipfile.ZipFile(zip_file_path, "w") as archive:
    for file in file_paths:
        archive.write(file)

with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    for info in zip_ref.infolist():
        print(
            f"Name: {info.filename}, Size: {info.file_size}, Compressed: {info.compress_size}"
        )

with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extract("example2.txt", "extracted")

with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    file_content = zip_ref.read("example1.txt")
    print(file_content.decode("utf-8"))

with open("example4.txt", "w") as file:
    file.write("Hello World")

with zipfile.ZipFile(zip_file_path, mode="a") as archive:
    archive.write("example4.txt")

with zipfile.ZipFile(zip_file_path, mode="r") as zip_ref:
    print(zip_ref.namelist())
