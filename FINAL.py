import re
import sys

print "Hi this is my commit"
f = open("10005_pg1.dat", "r")
fw = open("dumy.csv","w")
for line in f.readlines():
 line = line.strip()
 x = len(line)
 Sheet =line[1:40]
 District_code = line[40:44]
 Block_code = line[44:48]
 School_code = line[48:52]
 class_code = line[52:53]
 Section_code = line[53:54]
 Roll_no1 = line[54:79]
 Roll_no2 = line[79:104] 
 sex = line[104:129]
 Language = line[129:154]
 Number = line[154:179]
 Q1 = line[179:204]
 Q2 = line[204:229]
 Q3 = line[229:254]
 Q4 = line[254:279]
 


 print x
 print Sheet
 print District_code
 print Block_code
 print School_code
 print class_code
 print Section_code
 print Roll_no1
 print Roll_no2
 print sex
 print Language
 print Number
 print Q1
 print Q2
 print Q3
 print Q4
 print Q5
