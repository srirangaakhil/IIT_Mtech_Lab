import xmlrpc.client

if __name__ == '__main__':
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as server:
        n=server.ISPALIN(input())
        if n == 1:
            print("Yes")
        if n == 0:
            print("No")
        while n==1:
            n=server.ISPALIN(input())
            if n== 1:
                print("Yes")
            if n == 0:
                print("No")