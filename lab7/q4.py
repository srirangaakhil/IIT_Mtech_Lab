import sys
import numpy as np

class Student:
	num_students = 0
	def __init__(self, grades, credits):
		Student.num_students += 1
		self.grades = grades
		self.credits = credits

	def CPI(self):
		print(round(np.sum(np.dot(self.grades,self.credits))/np.sum(self.credits),4))

def main():
	a=[]
	b=[]
	c=[]
	j=0
	l=0
	i = 0
	with open(sys.argv[1], 'r') as f:
		for i in f:
			b.append(i.strip())
    
	for i in b:
		a=i.split(" ")
		c.append(a)
	f.close()
	students=[]
	#c = np.array(c, np.int64)
	for i in range(0,len(c),3):
		a=np.array(c[i],np.int64)
		b=np.array(c[i+1],np.int64)
		students.append(Student(a,b))
		j+=1
	print(Student.num_students)
	for i in range(j):
		students[i].CPI()

if __name__ == '__main__':
	main()