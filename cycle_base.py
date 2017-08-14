__author__ = 'am4613'

import os
import re
import csv

file_name = 'C:/Users/am4613/Documents/Summaries_as_timecourses/fission_timecourses/fission_metadata.tsv'

with open(file_name, 'r') as tsv:
    lines = [line.strip().split('\t') for line in tsv]

for i in range(0, len(lines)):
    lines[i] = line.replace('\{\}','')



