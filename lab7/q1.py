if __name__ == '__main__':
	input()
	for num in [int(i) for i in input().split(sep=' ')]:
		sqrt = int(num ** (1/2))
		if sqrt ** 2 == num:
			print(num, 'is a square number')
		else:
			print(num, 'is not a square number')