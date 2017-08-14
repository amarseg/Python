__author__ = 'am4613'

import os
import re
import csv

#This script changes the outline format from FISH-QUANT so that it matches Chad's Fiji Script for measurint outline area, length and width.
#With the new version it doesn't work as the format has changed slightly

folder = "C:\\Users\\am4613\\OneDrive\\FISH\\Outline\\"
file_list = os.listdir(folder)
file_list = [x for x in file_list if re.search('outline',x)]
os.mkdir(folder + 'New')
new_folder = folder + 'New\\'
for i in range(0,len(file_list)):
    with open(folder+file_list[i],"r") as input:
        with open(new_folder + file_list[i] + 'new.txt',"w") as output: 
            for line in input:
                if line!="CELL_END\n" and line != 'Z_POS\t\n':
                    if bool(re.search('X_POS', line)) or bool(re.search('Y_POS',line)):
                        new_line = line.rstrip() + '\tEND\t'
                        output.write(new_line)
                    elif bool(re.search('CELL', line)):
                        new_line = line.replace('CELL_START','CELL')
                        output.write(new_line)
                    else:
                        output.write(line)
                    
                    

# with open(folder+file_list[i],"r") as input:
#     content = input.readlines()