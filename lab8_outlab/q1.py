
def ISPALIN(str):
    flag = 0
    for j, k in zip(range(0, int(len(str) / 2) + 1, 1), range(int(len(str)) - 1, int(len(str) / 2) - 1, -1)):
        if str[j] != str[k]:
            flag = 1
    if flag == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range(0,n,1):
        a.append(input())

    for i in range(0,n,1):
        if ISPALIN(a[i]) == 1:
            print("Yes")
        if ISPALIN(a[i]) == 0:
            print("No")