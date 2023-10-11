#!/usr/bin/python3

import sys
import os

"""
FUNCTIONS
"""


def file_check(file_path=""):
    """check if a file path is valid"""
    basename = os.path.basename(file_path)
    directory = os.path.dirname(file_path)
    if not os.path.isfile(file_path):
        print("There is no {} in {}\nCheck the spelling"
              " if you think you have one".format(basename, directory), file=sys.stderr)
        sys.exit("Program terminated!")


def file_length_check(file_path=""):
    """checks the length of a file"""
    # basename = os.path.basename(file_path)
    # directory = os.path.dirname(file_path)

    with open(file_path, "r") as f:
        file_content = f.read()

    if len(file_content) == 0 or file_content == "\n":
        print("{} is empty".format(file_path), file=sys.stderr)
        sys.exit("Program terminated!")
    else:
        print("SUCCESS: The readme '{}' is non empty".format(file_path))


"""
Script
"""
if len(sys.argv) != 2:
    print("usage: check <dirpath>", file=sys.stderr)
    sys.exit("Program terminated!")

path = sys.argv[1]
if not os.path.isdir(path):
    print("{} is not a valid directory".format(path), file=sys.stderr)
    sys.exit("Program terminated!")

readme_path = os.path.join(path, "README.md")
file_check(file_path=readme_path)

file_length_check(file_path=readme_path)

all_subdirs = next(os.walk(path))[1]
valid_subdirs = [d for d in all_subdirs if d[0] != "."]

for subdir in valid_subdirs:
    readme_path = os.path.join(path, subdir, "README.md")
    file_check(file_path=readme_path)
    file_length_check(file_path=readme_path)

print("SUCCESS: ALL CHECKS COMPLETE!")
