import os

def loop_all_files(directory):
    path = []
    for file in os.listdir(directory):
        if file.endswith(('jpg', 'png', 'jpeg')):
            path.append(os.path.join(directory, file).replace('\\', '/'))
    return path

def create_folder_result(directory): # create folder to contain output data
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_files(filename): # read object detected
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content