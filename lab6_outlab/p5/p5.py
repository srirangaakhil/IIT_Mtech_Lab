import sys
from re import *
from collections import Counter

f = open(sys.argv[1], "r")

p = compile(r'(?:\b[a-zA-Z0-9]+(?:[._][a-zA-Z0-9]+)*@(?:[a-zA-Z0-9]+[.])*[a-zA-Z0-9]*[a-zA-Z]\b)|(?:\b[1-9][0-9]{9}\b)')

words = p.findall(f.read())

my_contact = str(sys.argv[2])
freq_dict = Counter(words)

print("my frequency: " + str(freq_dict[my_contact]))

ls = [(item, freq_dict[item]) for item in freq_dict if freq_dict[item] > freq_dict[my_contact] and item != my_contact]

if len(ls) > 0:
	for item in ls:
		print("Cheater alert! " + item[0] + " " + str(item[1]))
else:
	print("It’s all good yo!")


