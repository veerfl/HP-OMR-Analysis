import re
import sys
import csv


f = open("10005_pg1.dat", "r")
Roll_no1 = ''
Roll_no2 = ''
for line in f.readlines():
	line = line.strip()
	x = len(line)
	if x > 0:
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
		c = csv.writer(open("MYFILE.csv", "wb"))
		c.writerow(["Student Roll No","student_sex","student_Language","student_Number","Q1","Q2","Q3","Q4"])

		
		for y in range(0,25):
			student_roll_no = Roll_no1[y] + Roll_no2[y]
			student_sex = sex[y]
			student_Language = Language[y]
			student_Number = Number[y]
			student_Q1 = Q1[y]
			student_Q2 = Q2[y]
			student_Q3 = Q3[y]
			student_Q4 = Q4[y]
			#out =  'Student Roll No :' , student_roll_no,  ' Sex:', student_sex, 'Language:',student_Language, 'Number:', student_Number,'Q1',student_Q1,'Q2',student_Q2,'Q3',student_Q3,'Q4',student_Q4
			
			#print out
			c.writerow([student_roll_no,student_sex,student_Language,student_Number,student_Q1,student_Q2,student_Q3,student_Q4])
			
		
			 

		
			


			



 