# Script to renew the Adobe InDesign trial number.
# Automation can be carried out on OS level.

import re

TSN_LINE_NO = 5 # TSN (Trial Serial Number) located on line 5
TSN_WORD_NO = 23 # After parsing, TSN is word 23 of line 5
TSN_COL_NO = 232 # TSN begins from column 23

f = open("C:\Program Files\Adobe\Adobe InDesign 2021\AMT\\application.xml", "r")
f_lines = f.readlines()
f.close()

line = f_lines[TSN_LINE_NO].strip("\n|\t")
line_list = re.split(' |="|">|</', line) # Parsing and removing unnecessary characters

current_tsn = line_list[TSN_WORD_NO]
new_tsn = (int(line_list[TSN_WORD_NO]) + 1)

f_lines[TSN_LINE_NO] = f_lines[TSN_LINE_NO][:TSN_COL_NO] # Cut 916587039040963386426082</Data></Other> from end of line (example tsn)
f_lines[TSN_LINE_NO] += (str(new_tsn) + "</Data></Other>\n") # Replace with new tsn

fw = open("C:\Program Files\Adobe\Adobe InDesign 2021\AMT\\application.xml", "w")
for l in f_lines:
    fw.write(l)    
fw.close()
