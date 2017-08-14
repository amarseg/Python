__author__ = 'am4613'

import os
import re
import csv



def area_parser(path):

    with open (path, 'r') as f:
        file_content=f.readlines()
        
    new_file_name=os.path.dirname(path) + '//formatted_area.txt'
    output =  open(new_file_name,'w')
    file_writer = csv.writer(output, delimiter = '\t')
    file_writer.writerow(['Sample'] +['Cell']+['Area']+['Length']+['Width'])

    for i in range(0,len(file_content)):
        if bool(re.search('outline', file_content[i])):
            file_name=file_content[i].rstrip()
            file_name=(re.sub('\t','',file_name))
        elif re.search('Pixel', file_content[i]) or re.search('CELL',file_content[i]) or re.search('\t\t\t\n',file_content[i]):
            pass
        else:
            ToDo = file_content[i].split('\t')
            cell = ToDo[0]
            area = ToDo[1]
            length = ToDo[2]
            width = ToDo[3].rstrip()
            file_writer.writerow([file_name] + [cell]+[area]+[length]+[width])
    output.close()

folder = "C:\\Users\\am4613\\OneDrive\\FISH\\Outline\\New\\wtf.txt"
area_parser(folder)