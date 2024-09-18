#!/usr/bin/python

import sqlite3

import sys

import csv

import numpy as np

class Employee:
	def __init__(self):
		#self.name = name
		#self.idt = idt
		#self.salary = salary
		#self.city = city
		conn = sqlite3.connect('employeeDB.db')

		conn.execute('''CREATE TABLE employeeInfo
        	(NAME           TEXT,
        	ID            INT ,
			SALARY         INT,
			CITY        TEXT);''')

		conn.close()


	def populate_table(self,file):
		name=[]
		idt=[]
		sal=[]
		city=[]
		with open(file,'rt')as f:
			data = csv.reader(f)
			for row in data:
				b=row
				name.append(b[0])
				idt.append(b[1])
				sal.append(b[2])
				city.append(b[3])
		conn = sqlite3.connect('employeeDB.db')
		for i in range(1,len(name),1):
			conn.execute("INSERT INTO employeeInfo (NAME,ID,SALARY,CITY) \
			VALUES (?,?,?,?)",(name[i],idt[i],sal[i],city[i]))
		conn.commit()
		conn.close()

	def print_all(self):
		conn = sqlite3.connect('employeeDB.db')
		cursor = conn.execute("SELECT name, id, salary,city from employeeInfo")
		for row in cursor:
			print(row[0],",",row[1],",",row[2],",",row[3])
		conn.close()

	def highest_salary(self):
		conn = sqlite3.connect('employeeDB.db')
		cursor = conn.execute("SELECT name, id, salary,city from employeeInfo where salary=(select max(salary) from employeeInfo)")
		for row in cursor:
			print(row[0],",",row[1],",",row[2],",",row[3])
		conn.close()



def main():
	file=' '.join(sys.argv[1:])
	obj=Employee()
	obj.populate_table(file)
	obj.highest_salary()
	obj.print_all()


if __name__ == '__main__':

	main()
