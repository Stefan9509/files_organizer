'''
Input data:
    - Path of the folder

Output data:
    - Move files in the specific folder
'''

import os
import shutil


def path_route():
    # Insert the path of the folder where is need to arrange the items
    insert_path = input('Insert the path or press Q to exit the program: ')
    while not path_validation(insert_path):
        if insert_path == 'Q':
            exit()
        insert_path = input('Insert the path or press Q to exit the program: ')

    print('The path is valid')
    return insert_path


def path_validation(path: str) -> bool:
    # Path validation
    return os.path.isdir(path)


def map_folder_and_extension(path: str) -> dict:
    # Using dictionary comprehension is creating a dict with folders and their corresponding extensions
    ext_folder_mapping = {path + '\\' + dir: EXTENSION_TYPES[i] for i, dir in enumerate(DIR_NAMES)}
    return ext_folder_mapping


def create_directories(path: str):
    # Creating folders if doesn't exist
    for dir in DIR_NAMES:
        if not os.path.isdir(path + '\\' + dir):
            os.mkdir(path + '\\' + dir)


def list_files(path: str) -> list:
    # Search all files from path
    files = [file for file in os.listdir(path) if os.path.isfile(path + '\\' + file)]
    return files


def extraction_extension(file: str):
    # Find the extension of the files
    indexes = [i for i, character in enumerate(file) if character == '.']
    if indexes:
        file_extension = file[indexes[-1]::]
        return file_extension
    else:
        return 'The extension does not correspond with extensions searched'


if __name__ == '__main__':
    # Folder name new created
    DIR_NAMES = ['Pictures', 'Videos', 'PDF_files', 'Word_files', 'Excel_files', 'Archived_files', 'Music', 'TXT_files',
                 'Python_files', 'Exe_files']

    # Extensions name
    EXTENSION_TYPES = [['.jpg', '.jpeg', '.png', '.JPG'], ['.mp4', '.mov', '.MOV', '.avi'], ['.pdf', '.PDF'],
                       ['.doc', '.docx'], ['.csv', '.xls', 'xlsx'], ['.zip', '.7z'], '.mp3', '.txt', '.py', '.exe']

    path = path_route()
    mapping = map_folder_and_extension(path)

    create_directories(path)
    files = list_files(path)

    for file in files:
        file_extension = extraction_extension(file)

        for k, v in mapping.items():
            if file_extension in v:
                try:
                    shutil.move(path + '\\' + file, k)
                except:
                    print(file + ' does not moved')
