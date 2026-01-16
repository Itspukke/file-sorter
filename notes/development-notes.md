# File Sorter Project – Development Notes

## Project Purpose
The purpose of this project is to automate file organization within a folder by sorting files into different directories based on their file extensions.

This project was inspired by the common problem of having a cluttered Downloads folder where different file types are mixed together.

---

## Tools and Technologies Used
- Python
- os module
- shutil module

---

## Folder Path Configuration
The script uses a fixed folder path that points to the directory that needs to be sorted.

```python
path = r"C:/Users/shampie/Downloads/FileSorter/"


**Folder Creation Logic**

A list is used to store folder names for different file types:
folder_names = ["xlsx files", "pdf files", "png files", "docx files"]

A loop checks whether each folder exists.
If a folder does not exist, it is created automatically using os.makedirs().

This ensures that the script does not fail when run for the first time.


**File Detection and Sorting Logic**

The script scans all files in the target directory using:
os.listdir(path)

Each file is checked for a specific file extension:
.pdf
.png
.docx
.xlsx

Conditional statements are used to determine the correct destination folder.

Example:

if ".pdf" in file:
    shutil.move(path + file, path + "pdf files/" + file)

Files are only moved if they do not already exist in the destination folder.
This helps prevent errors caused by duplicate files.


**Screenshots Documentation**

Screenshots were taken before and after running the script to visually demonstrate the effectiveness of the automation.

-Before Screenshot: Shows a cluttered folder with mixed file types.

-After Screenshot: Shows files successfully organized into separate folders.

These screenshots are included in the "Screenshots" folder for easy viewing.


**Challenges Faced**

-Ensuring folders exist before moving files.
=Preventing files from being moved multiple times.
-Working with file paths correctly in Windows.


**How the Challenges Were Solved**

-Used os.path.exists() to check for folders and files.
-Used conditional logic to avoid overwriting files.
-Used raw strings (r"...") to avoid path errors.


**What I Learned**

-How to work with the operating system using Python.
-How to automate repetitive manual tasks.
-How to safely move files between directories.
-The importance of documenting code and processes.


This project helped reinforce practical Python skills and demonstrated how automation can be used to solve real-world problems efficiently.