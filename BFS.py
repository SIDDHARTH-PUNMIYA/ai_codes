node = int(input("ENTER THE NUMBER OF NODES  IN THE GRAPH "))
# L = [[]] * node
#
# # creation of graph
# for i in range(node):
#     for j in range(node):
#         L[i].append(int(input("ENTER THE EDGE VALUE FOR  {}".format(i))))
L=[ [0,1,0,0,0,0],
    [1,0,1,1,0,0],
    [0,0,0,1,0,0],
    [0,1,0,0,1,0],
    [0,0,0,0,0,0],
    [0,0,1,0,0,0]
    ]


# main implementation
def bfs(node, L):
    n = int(input("ENTER THE SRC NODE FROM 0 TO {}".format(node)))
    queue = [n]
    res = [True] * node
    res[n] = False
    f = 1
    des=int(input("ENTER THE Dest NODE FROM 0 TO {}".format(node)))
    while len(queue) != 0:
        var = queue.pop(0)
        if var == des:
            f = 0
            break
        for j in range(len(L[var])):
            if (L[var][j] == 1 and res[j] == True):
                queue.append(j)
                res[j] = False
        print(queue)
    if f == 0:
        print("The destination is  found")


bfs(node, L)