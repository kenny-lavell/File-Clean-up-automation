# File Organizer Script

Overview

This Python script automates the process of organizing files in a specified folder by sorting them into subfolders based on their file extensions. It helps declutter directories and improve file management efficiency.

Features

Automated Sorting:

Files are categorized into subfolders like Images, Documents, Audio, Videos, Archives, and Others.

Customizable Categories:

Easily modify the file categories and their extensions in the script.

Error Handling:

Ensures the specified folder path exists before attempting to organize files.

Requirements

Python Version: Python 3.6 or higher

Libraries:

os (built-in)

shutil (built-in)

How to Use

Set Folder Path:

Update the folder_to_organize variable in the script with the path to the folder you want to organize. For example:

folder_to_organize = r"C:/Users/YourUsername/Downloads"

Run the Script:

Execute the script in your Python environment or terminal.

Organized Output:

Files in the specified folder will be moved into subfolders based on their extensions.

Folder Categories

The script currently categorizes files into the following groups:

Images: .jpg, .jpeg, .png, .gif, .bmp

Documents: .pdf, .doc, .docx, .txt, .xlsx, .csv

Audio: .mp3, .wav, .aac

Videos: .mp4, .mkv, .avi, .mov

Archives: .zip, .rar, .tar, .gz

Others: Any files that don't match the above extensions

Example Output

Before running the script:

Downloads/
├── file1.jpg
├── file2.pdf
├── song.mp3
├── video.mp4
├── archive.zip

After running the script:

Downloads/
├── Images/
│   └── file1.jpg
├── Documents/
│   └── file2.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── video.mp4
├── Archives/
│   └── archive.zip

Customization

You can customize the file categories by modifying the file_categories dictionary in the script.

Troubleshooting

Error: Folder does not exist

Ensure the folder_to_organize variable contains the correct path.

Files not moving:

Check for file permissions or open files that might prevent movement.

License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
