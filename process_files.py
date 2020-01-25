import os
import zipfile
from shutil import copyfile


def get_name_and_extension(file_name):
    """
    get name and extension of a file_name
    :param file_name:
    :return:
    """
    tokens = file_name.split('.')
    return {'name': '.'.join(tokens[0:-1]), 'ext': tokens[-1]}


def process_data(input_folder, data):
    std_name = ''
    for line in data:
        if 'Name:' in line:
            tk = line.split(' ')
            for i in range(1,len(tk)):
                std_name += tk[i] + '_'
            std_name = std_name.split('\n')[0]
        if 'Filename:' in line:
            fname = line.split('Filename: ')
            fname = fname[1].split('\n')[0]
            
            if '.zip' in fname:
                pass
                with zipfile.ZipFile(os.path.join(input_folder + fname), 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(input_folder+'files/'+std_name))
            elif '.rar' in fname:
                print('------------------------------------------')
                try:
                    os.mkdir(os.path.join(input_folder+'files/'+std_name))
                except:
                    print('files/'+std_name + ' folder exists')
                print(fname + ' is a rar file. Please unrar manually and copy to ' + 'files/'+std_name)
                print('------------------------------------------')
            else:
                print('------------------------------------------')
                try:
                    os.mkdir(os.path.join(input_folder+'files/'+std_name))
                except:
                    print('files/'+std_name + ' folder exists')
                print(fname + ' is not a zip file. Please manually handle and copy to ' + 'files/'+std_name)
                print('------------------------------------------')


def process_files(input_folder):
    ind = 1
    for filename in os.listdir(input_folder):
        name_extension = get_name_and_extension(filename)
        name = name_extension['name']
        ext = name_extension['ext'].lower()

        if ext == 'txt':
#             print(ind, ":", filename)
            ind += 1

            try:
                with open(os.path.join(input_folder, filename), 'r') as info_file:
                    process_data(input_folder, info_file)
            except:
                print(filename + ' not found!')


def file_structure(input_folder):
    try:
        os.mkdir(os.path.join(input_folder+'files/'))
    except:
        print("Couldn't create 'files' folder to unzip files")
    for filename in os.listdir(input_folder):
        for dirpath, subdir, files in os.walk(input_folder+filename):
            for f in files:
                if f == 'search.py':
                    try:
                        copyfile(os.path.join(dirpath, f), input_folder+filename+'/'+f)
                    except:
                        pass
                elif f == 'searchAgents.py':
                    try:
                        copyfile(os.path.join(dirpath, f), input_folder+filename+'/'+f)
                    except:
                        pass
                    
process_files('raw/')

file_structure('raw/files/')


