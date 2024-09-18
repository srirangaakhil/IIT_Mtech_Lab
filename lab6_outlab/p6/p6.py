import argparse
import csv
import os.path
from os import path
import sys

def read_data(filename,lastname,roll_no,gender,mobile,dept,CGPA):
	row = [filename,lastname,roll_no,gender,mobile,dept,CGPA]
	firstline = ["filename","lastname","roll_no","gender","mobile","dept","CGPA"]
	if path.exists("student_database.csv"):
		with open('student_database.csv', 'a') as csvFile:
   			writer = csv.writer(csvFile)
   			writer.writerow(row)
	else:

		with open('student_database.csv', 'w') as csvFile:
   			writer = csv.writer(csvFile)
   			writer.writerow(firstline)
   			writer.writerow(row)
	csvFile.close()

def main():

	fn=args.firstname
	ln=args.lastname
	rn=args.roll_no
	g=args.gender
	m=args.mobile
	d=args.dept
	c=args.CGPA
	if fn is None or ln is None or rn is None or g is None or m is None or d is None or c is None:
		print("the following arguments are required:", end="")
		if fn is None:
			sys.stdout.write(" firstname,")
		if ln is None:
			sys.stdout.write(" lastname,")
		if rn is None:
			sys.stdout.write(" roll_no,")
		if g is None:
			sys.stdout.write(" gender,")
		if m is None:
			sys.stdout.write(" mobile,")
		if d is None:
			sys.stdout.write(" dept,")
		if c is None:
			sys.stdout.write(" CGPA,")
		sys.stdout.write("\b ")
		print()
		return	

		
	read_data(args.firstname,args.lastname,args.roll_no,args.gender,args.mobile,args.dept,args.CGPA)

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--firstname', type=str)
	parser.add_argument('--lastname', type=str)	
	parser.add_argument('--roll_no', type=int)
	parser.add_argument('--gender', type=str)
	parser.add_argument('--mobile', type=str)
	parser.add_argument('--dept', type=str)
	parser.add_argument('--CGPA', type=str)
		

	args = parser.parse_args()

	main()
