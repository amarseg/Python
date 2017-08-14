__author__ = 'am4613'

import os
##Input: folder with outline files from FISH-QUANT
##Output: Create new outline files with the name of the other channels to import
##IMPORTANT!!! WORKS ONLY WITH LIF_EXTRACTOR OUTPUT
def name_changer(folder):
    file_list = os.listdir(folder)
    for i in range(0, len(file_list) - 1):
        with open (folder + file_list[i],'r') as f:
            content = f.readlines()
        chunk = content[3]
        trozos = chunk.split('=')[0]
        for j in range(1,4):
            new_content = content
            new_content[3] = trozos + '=' + str(j) + '.tif\n'
            basename = file_list[i].split('=')[0]
            new_filename = basename + '=' + str(j) + '__outline.txt'
            with open (folder + str(new_filename),'w+') as f:
                for item in new_content:
                    f.write(item)
    return j



folder = "C:\\Users\\am4613\\OneDrive\\FISH\\Outline2\\"
name_changer(folder)