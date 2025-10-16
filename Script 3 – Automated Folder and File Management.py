# I thought it was best to use the os package as it can be used on both windows and linux.
# This way the correct path format will be used depending on whether the user is using linux/windows.
# I mostly referenced slides from Lecture 13-15 as these covered reading and writing to the OS and lists.
# I have referenced specific sources throughout my code.

# I prompted the user to enter the folder name in the main function.
# After this the folder name is used as a parameter in each function.
#
# First I call the create_folder function.
# I wanted the user input to be created as a folder automatically.
# First the function checks if the folder already exists, if so it is deleted.
# Now the folder is created. This was done using mkdir and the user input.
# For the subfolders and files I needed to create what I did is create a few lists for them
# In each list I had it iterate through the files/folders in the list.
# For the folders I would create the folders and the folder path.
# For the files I would open each one with a write connection and write the filename to the file
# This is so each file has varying content.

# Then rename_docs_files function is called.
# The first thing I did was ensure the docs folder exists.
# If it doesn't I want the function to end to I used return.
# If this wasn't the case I iterated through the relevant files.
# For each file I saved the old file path and created a new one with lowercase letters using .lower
# I then used split at the end of the filename at the . and adding TXT
# Using path join I got the full file path for the file I renamed.
# Using os.rename I finalised the renaming.
#
# When the above is complete then the backup_docs function is called.
# Using os path join I make 3 different folder paths for my docs folder, backup folder and docs_backup.zip
# Using zipfile I open the file in write mode.
# I get the current file path using os.path.join
# I find the relative path of file from the docs folder using relpath
# I then write the file to the zip folder I made previously using the relative path I just found
# I use a print statement to confirm the backup was successful.
#
# Lastly the list_content function is called.
# I use os.path.join to get the path of the backup folder
# I then iterate through each file in the backup folder and print it

import os, shutil
import zipfile


def create_folder(folder_name):
    # Checking if folder exists, if so deleting it
    if os.path.exists(folder_name):   # Source: Lecture 14 - Slide 13
        print(f"Deleting existing folder {folder_name}...")
        shutil.rmtree(folder_name)  # Source: Question 1 - Lab 10
        
    # creating the main folder
    os.mkdir(folder_name)  # Source: Lecture 14 - Slide 10
    print(f"Created folder {folder_name}.")

    # creating a list of subfolders
    subfolder_list = ['backup', 'working']  # Source: Lecture 13 - Slide 4
    # creating folders in main folder
    for subfolder in subfolder_list:  # iterating through each folder in the list
        # Source: Lecture 14 - Slide 4 and 10
        os.mkdir(os.path.join(folder_name, subfolder))  # creating said folder in this path
        print(f"Created folder '{subfolder}' in the {folder_name} folder.")

    # making subfolders inside the working folder
    working_folder = os.path.join(folder_name, 'working')  # Source: Lecture 14 - Slide 4
    # creating a list of folders
    working_subfolders = ['pics', 'docs', 'movie']
    for subfolder in working_subfolders:  # iterating through each folder in the list
        # Source: Lecture 14 - Slide 4 and 10
        os.mkdir(os.path.join(working_folder, subfolder))  # creating said folder in this path
        print(f"Created subfolder '{subfolder}' inside working folder.")

    # making a file path string with the input
    docs_folder = os.path.join(working_folder, 'docs')  # Source: Lecture 14 - Slide 4
    # creating files inside docs folder
    files = ['SCREENTIME.txt', 'DANGEROUS.txt', 'KEEPSAFE.txt', 'CONCENTRATE.txt', 'SUCCEED.txt']
    for filename in files:  # iterating through each file
        # Opening file in write mode
        with open(os.path.join(docs_folder, filename), 'w') as file:  # Source: Lecture 14 - Slide 4
            file.write(f"This .txt file is called {filename}.")  # Writing the filename on the file2
            print(f"Created file {filename} inside docs folder.")

    # creating subfolders inside docs folder
    docs_subfolders = ['school', 'party']
    for subfolder in docs_subfolders:  # iterating through each folder
        # Making a directory for the subfolder in the docs folder
        os.mkdir(os.path.join(docs_folder, subfolder))
        print(f"Created subfolder {subfolder} inside docs folder.")


def rename_docs_files(folder_name):
    # Path is made to the docs folder inside the working folder within the user inputted folder
    docs_folder = os.path.join(folder_name, 'working', 'docs')  # Source: Lecture 14 - Slide 4
    if not os.path.exists(docs_folder):  # Checking if the path exists (Source: Lecture 14 - Slide 13)
        print("Docs folder does not exist.")
        return  # exit function

    for root, dirs, files in os.walk(docs_folder):
        for file in files:
            # Getting the full file path
            old_file_path = os.path.join(root, file)  # Source: Lecture 14 - Slide 4
            new_file_name = file.lower()  # converting the filename string to lowercase

            # Splitting the filename at the . and adding TXT
            new_file_name = new_file_name.split('.')[0] + '.TXT'  # changing txt to uppercase

            # Getting the full file path for the renamed file
            new_file_path = os.path.join(root, new_file_name)  # Source: Lecture 14 - Slide 4
            os.rename(old_file_path, new_file_path)  # renaming it by moving it to the new path
            print(f"Renamed file '{file}' to '{new_file_name}'.")


def backup_docs(folder_name):
    # Path is made to the docs folder inside the working folder within the user inputted folder
    docs_folder = os.path.join(folder_name, 'working', 'docs')  # Source: Lecture 14 - Slide 4

    # Path is made inside the backup folder within the user inputted folder
    backup_folder = os.path.join(folder_name, 'backup')

    # Making 5 zip backups
    for i in range(1,6):
        # making filename for the zip archive
        zip_filename = os.path.join(backup_folder, f'docs_backup{i}.zip')   # Source: Slide 17 - Lecture 15
        # Opening file in write mode
        with zipfile.ZipFile(zip_filename, 'w') as zipf:   # Source: Slide 17 - Lecture 15
            for root, dirs, files in os.walk(docs_folder):
                for file in files:  # Iterating through each file

                    # Getting current file path
                    file_path = os.path.join(root, file)  # Source: Lecture 14 - Slide 4

                    # Relative path of file from the docs folder
                    arcname = os.path.relpath(file_path, start=docs_folder)  # Source: Lecture 14 - Slide 8
                    # Writing the file to the zip using the relative path
                    zipf.write(file_path, arcname=arcname)  # Source: Slide 17 - Lecture 15

    print(f"Backup made: {zip_filename}")


def list_content(folder_name):
    backup_folder = os.path.join(folder_name, 'backup')  # Source: Lecture 14 - Slide 4
    print("Backup folder contents:")
    # Iterating through each file in the backup folder and printing it
    for file in os.listdir(backup_folder):  # Source: Lecture 14 - Slide 11
        print(file)


if __name__ == '__main__':
    folder = input(f"Enter a folder name: ")  # Folder is passed as a parameter to all functions
    create_folder(folder)
    rename_docs_files(folder)
    backup_docs(folder)
    list_content(folder)
