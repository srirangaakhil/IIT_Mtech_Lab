from functools import reduce

def collapse(L):
    return reduce(lambda a,b : a+' '+b,reduce(lambda a,b:a+b,L))


