# file-sorter

## Python Script for Organizing Files by Extension

This Python script organizes files in a specified folder by their extensions. It does so by creating separate folders for each unique file extension and moving the respective files into those folders.

### Features:
- Automatically identifies the extensions of files in the given folder.
- Creates a dedicated folder for each file extension (e.g., .txt files are moved to a folder named txt_files).
- Moves all files into the corresponding folder based on their extension.
- Ensures no duplicate folders or overwriting occurs if the file already exists in the destination folder.

### How to Use:

- Run the script in Python.
- When prompted, input the full path of the folder that contains the files you wish to organize.
- The script will create new folders inside the specified folder for each file type (based on the extension) and move the files accordingly.

### Requirements:

Python 3.x
os and shutil libraries (these are built-in in Python, so no external dependencies are required).
