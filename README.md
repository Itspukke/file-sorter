# 📂 File Sorter Automation Script

# 📌 Project Overview

This project is a Python automation script that organizes files in a specified folder by sorting them into separate folders based on file type.

It was created to solve the problem of cluttered folders (such as the Downloads folder) where files like PDFs, images, and documents are mixed together.


# 🎯 Problem Statement

Manually sorting files is time-consuming and inefficient.
This script automates the process by detecting file extensions and moving files into appropriate folders automatically.


# 🛠️ Technologies Used

-Python
-os module (for file and folder handling)
-shutil module (for moving files)


# ⚙️ How the Script Works

1)The script scans a target directory.
2)It checks if folders for specific file types exist.
3)If the folders do not exist, they are created automatically.
4)Files are identified by their extensions.
5)Files are moved into their corresponding folders.


# 📁 File Types Supported

The script currently sorts the following file types:

.pdf → pdf files

.png → png files

.docx → docx files

.xlsx → xlsx files


# 🖼️ Screenshots

**#Before Sorting#**

This screenshot shows the folder before running the script, where all file types are mixed together.

**#After Sorting#**

This screenshot shows the folder after the script has been executed.
Files are automatically organized into folders based on their file types.



# ▶️ How to Run the Project

1)Clone the repository:git clone https://github.com/your-username/file-sorter.git

2)Open the script and update the folder path if needed:path = r"C:/Users/your-username/Downloads/FileSorter/"

3)Run the script:sorter.py


# 💡 What I Learned

-How to automate file management using Python.
-Working with directories and file paths.
-Creating folders programmatically.
=Using conditional logic to handle different file types.



# 🚀 Future Improvements

-Add support for more file types.
-Handle duplicate filenames.
-Allow the user to choose the directory dynamically.
-Schedule automatic sorting


# 👤 Author

Tshedza Tshipuke

Aspiring Data Analyst | Python, SQL & PowerBI Enthusiast
