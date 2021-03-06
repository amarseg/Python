__author__ = 'am4613'

import os
import re
import csv

def spot_counter(folder):
    file_list = os.listdir(folder)
    file_list = [x for x in file_list if re.search('spots',x)]
    for j in range(0,len(file_list)):

        filename = file_list[j].split('_')
        sample_name = filename[0]
        mix = filename[1]

        series = filename[2].split('-')

        date = series[0]
        picture = series[1]
        channel = series[2].split('=')[1]
        cell_names = list()
        cell_spots = list()

        spots = 0
        count = False
        with open (folder + file_list[j],'r') as f:
            file_content = f.readlines()
        file_content.append('')
        for i in range(0,len(file_content)):
            if bool(re.search('CELL', file_content[i])):
                cell_names.append(file_content[i].split('\t')[1])
                count = False
                cell_spots.append(spots - 3)
                spots = 0
            if bool(re.search('Y_POS',file_content[i])) and bool(re.search('SPOTS', file_content[i+1])):
                count = True

            elif bool(re.search('Y_POS',file_content[i])) and not bool(re.search('SPOTS', file_content[i+1])):
                spots = 3
            if count:
                spots += 1
        cell_spots.append(spots - 3)

        with open(folder + 'Results_'+ file_list[j],'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter = '\t')
            filewriter.writerow(['Sample_Name']+['Mix']+['Date']+['Picture']+['Channel']+['Cell']+['Spots'])
            for i in range(0,len(cell_names)):
                filewriter.writerow([sample_name] + [mix] + [str(date)] + [picture] + [str(channel)] + [cell_names[i].rstrip()] + [str(cell_spots[i+1])])


folder = "C:\\Users\\am4613\\Desktop\\FISH_QUANT\\Results_mature\\sho3_mix3\\"

spot_counter(folder)