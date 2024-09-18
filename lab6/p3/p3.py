
def genPrime(n):
	ls = list(range(2, n+1))
	fun1 = lambda l, x: list(filter(lambda y: (y == x or y%x != 0), l))
	fun2 = lambda l, i: l if len(l) == 0 or i == len(l) - 1 else fun2(fun1(l, l[i]), i+1)
	return fun2(ls, 0) 
