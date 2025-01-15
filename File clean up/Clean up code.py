import os
import shutil


# Define the folder to organize
def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist. Please check the path and try again.")
        return

    # Create a dictionary to categorize files
    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Others': []
    }

    # Get a list of all files in the directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        file_path = os.path.join(folder_path, file)
        file_extension = os.path.splitext(file)[1].lower()

        # Determine the category for the file
        category_found = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                category_found = True
                category_folder = os.path.join(folder_path, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                shutil.move(file_path, os.path.join(category_folder, file))
                break

        # If the file doesn't match any category, move it to 'Others'
        if not category_found:
            others_folder = os.path.join(folder_path, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, file))

    print(f"Files in '{folder_path}' have been organized.")


# Example usage
if __name__ == "__main__":
    folder_to_organize = r"C:\Users\klave\Downloads"  # Replace with your folder path