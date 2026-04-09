import os


def read_line(file):
    with open(file, "r") as file:
        for l in file:
            print(l, end="")


def read_line_yield(file):
    with open(file, "r") as file:
        for l in file:
            yield l.rstrip("\n")


file_generator = read_line_yield("example4.txt")
for line in file_generator:
    print(line)
