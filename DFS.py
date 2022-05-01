node = int(input("ENTER THE NUMBER OF NODES  IN THE GRAPH "))

L=[ [0,1,0,0,0,0],
    [1,0,1,1,0,0],
    [0,0,0,1,0,0],
    [0,1,0,0,1,0],
    [0,0,0,0,0,0],
    [0,0,1,0,0,0]
    ]
src = int(input("ENTER THE SRC NODE FROM 0 TO {}".format(node)))
des = int(input("ENTER THE Dest NODE FROM 0 TO {}".format(node)))
def dfs(node,L,n,des):

    stack = [n]
    f=1
    res = [True] * node
    res[n] = False

    while len(stack) != 0:
        var = stack.pop()
        # print(var)
        if (var == des):
            f=0
            break
        for j in range(len(L[var])):
            if L[var][j] == 1 and res[j] == True :
                stack.append(j)
                res[j] = False
        print("The stack is {}".format(stack))
    if f == 0 :
        print("the path is present")
    else :
        print("No path present")

def recur(node,L,src,des,res):
    if src == des:
        return True
    for j in range(len(L[src])):
        if L[src][j] == 1 and res[j]==True :
             res[j]=False
             data = recur(node,L,j,des,res)
             if data:
                return True
    return False



def recur_help():
    res = [True] * node
    res[src] = False
    print("Path is ")
    print(recur(node, L, src, des,res))


recur_help()
dfs(node, L,src,des)