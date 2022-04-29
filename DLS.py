graph=[[0,4,3,0,0,0,0],
       [0,0,0,0,12,5,0],
       [0,0,0,7,10,0,0],
       [0,0,0,0,2,0,0],
       [0,0,0,0,0,0,5],
       [0,0,0,0,0,0,16],
       [0,0,0,0,0,0,0]]

n=len(graph)


def dls(s,g,d):
        stack=[]
        td=0
        depth=[1000]*n
        depth[s]=0
        stack.append(s)
        visited=[]
        flag=-1
        print("Route :")
        while(len(stack)!=0):
            node=stack.pop()
            visited.append(node)
            print(node ,end="  ")
            if node==g:
                flag=1
                print("\nGoal Node Found at Depth {}".format(depth[g]))
                break
            if depth[node]<d:
                for i in range(n):
                    if graph[node][i]>0 and i not  in visited:
                        stack.append(i)
                        depth[i]=depth[node]+1

        if flag==-1:
            print("\nGoal Node Not Found")

def inputdata():
    s=int(input("Enter the Start node "))
    g=int(input("Enter the Goal Node "))
    d=int(input("Enter the Max Depth "))
    dls(s,g,d)

inputdata()