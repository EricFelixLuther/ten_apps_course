import os
import datetime
mypath = '/home/eric/python/ten_apps_course/'

def get_files(path, extension):
    found_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and extension in f]
    found_files.sort()
    return found_files


def concat_files_contents(path, files):
    content = []
    for file in files:
        with open(path + file, 'r') as f:
            content.append(f.read())
    content = '\n'.join(content)
    return content


def write_into_file(path, content):
    file_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    with open(path + file_name + '.txt', 'w') as f:
        f.write(content)


write_into_file(mypath, concat_files_contents(mypath, get_files(mypath, '.txt')))
