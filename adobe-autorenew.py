# Script to renew the Adobe InDesign trial number.
# Automation can be carried out on OS level.

import re

f = open("C:\Program Files\Adobe\Adobe InDesign 2021\AMT\\application.xml", "r")
f_lines = f.readlines()
f.close()

# Line 5 is where trial serial number is located
line = f_lines[5].strip("\n|\t")
line_list = re.split(' |="|">|</', line)

# Index of tsn is 23
current_tsn = line_list[23]
new_tsn = (int(line_list[23]) + 1)

f_lines[5] = f_lines[5][:232] # Cut 916587039040963386426082</Data></Other> from end of line (example tsn)
f_lines[5] += (str(new_tsn) + "</Data></Other>\n") # Replace with new tsn

fw = open("C:\Program Files\Adobe\Adobe InDesign 2021\AMT\\application.xml", "w")
for l in f_lines:
    fw.write(l)
    
fw.close()
