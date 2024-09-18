import urllib.request
import sys
from re import *

x = urllib.request.urlopen('https://www.cse.iitb.ac.in/page222?batch=MTech1')
p = compile(r'/~.*' + sys.argv[1])
words = p.findall(x.read().decode('utf-8'))
if len(words) == 0:
	print("Error: Name not found")
else:
	print(words[0].split('~')[1].split("'")[0] )		
