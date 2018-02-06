#!/usr/bin/python
#--coding=UTF8--
import os, sys

f1 = file("countingreport.txt",'w')
extension_name = ['py', 'cpp', 'c','h','cc','java','js', 'sh']

#########################################################
extention_set = set()
for i in extension_name:
	extention_set.add(i)

filecount = 0
dircount = 0
linecount = 0


def isCodingFile(filename):
	ex_name = os.path.splitext(filename)
	ex_name =  ex_name[1].split('.')[-1]
	if ex_name in extention_set:
		return True
	return False

def counting(cpwd):
	global filecount, dircount, linecount
	
	if os.path.isdir(cpwd) == True:
		dircount += 1
		
		for p in os.listdir(cpwd):
			tmp_pwd = os.path.join(cpwd, p)
			counting(tmp_pwd)

	else:
		if not isCodingFile(cpwd):
			return
		
		filecount += 1
		f2 = file(cpwd)
		tmpcount = 0
		while 1:
			line = f2.readline()
			if len(line) == 0:
				break
			tmpcount += 1
		f2.close()
		linecount += tmpcount
		f1.write(cpwd + "  " + str(tmpcount)+'\n')
		#f1.write(cpwd + "  " + str(os.stat(cpwd)[0])+'\n')


if len(sys.argv) == 1:
	print "Usage : $ python CodeLinesCounter.py file(directory)name1 file(directory)name1 ... "		

input_name = sys.argv[1:]
input_list = ""
for name in input_name:
	counting(name)
	input_list = input_list + " " + name

print "######[Done]######"
print "Input File	:" + input_list
print "Count of directory	:" + str(dircount)
print "Count of file	:" + str(filecount)
print "Count of line	:" + str(linecount)
print "Refer to countingreport.txt for details."

f1.close()
