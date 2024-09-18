from xmlrpc.server import SimpleXMLRPCServer

def ISPALIN(str):
    flag = 0
    for j, k in zip(range(0, int(len(str) / 2) + 1, 1), range(int(len(str)) - 1, int(len(str) / 2) - 1, -1)):
        if str[j] != str[k]:
            flag = 1
    if flag == 0:
        return 1
    else:
        return 0


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(ISPALIN, "ISPALIN")
server.serve_forever()