input_str = input()
res_dict = {}

def sort(x):
	return (x[0], x[1])	

for char in input_str:
	res_dict[char] = res_dict.get(char, 0) + 1; 


listofTuples = sorted(res_dict.items(), reverse=True, key=lambda x: (x[1], x[0]))
 
for elem in listofTuples:
    print(elem[0] + ": " + str(elem[1]) )   



