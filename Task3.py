import glob
import os

def get_file_paths():
    files_path = os.getcwd() + "/TASK3/"
    file_paths = glob.glob(files_path + "*.txt")
    return file_paths

def read_file():
    file_paths = get_file_paths()
    file_content = []
    for file in file_paths:
        file_name = file.split('/')[-1]
        with open(file, encoding="utf-8") as f:
            data = f.readlines()
            file_content.append([len(data), file_name, data])
    file_content.sort()
    with open ("result path.txt", "w", encoding="utf-8") as result_f:
        for item in file_content:
            result_f.write(f'{item[0]}/n {item [1]}\n {" ".join(item[2])}\n')
    return file_content 
print(read_file())
read_file()