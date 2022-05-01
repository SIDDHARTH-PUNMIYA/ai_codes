# graph=[[0,4,3,0,0,0,0],
#        [0,0,0,0,12,5,0],
#        [0,0,0,7,10,0,0],
#        [0,0,0,0,2,0,0],
#        [0,0,0,0,0,0,5],
#        [0,0,0,0,0,0,16],
#        [0,0,0,0,0,0,0]]
graph=[[0,7,3,0,0,0,0],
       [0,0,0,0,6,0,0],
       [0,2,0,9,0,0,0],
       [0,0,0,0,3,0,0],
       [0,0,0,0,0,2,1],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]

md=int(input("Enter the Maximum Depth to br Explored"))
md=md+1
r=int(input("Enter the Root node"))
goal=int(input("Enter the goal node"))
stack=[]
d=[]
l=[r]
d.append(l)
f=0
for i in range(md-1):

    if f == 1:
        break
    print("Iteration {}".format(i+1))
    stack.append(r)
    visited=[]
    while (len(stack)!=0):
        node=stack.pop()
        if node == goal :
            print(node)
            f=1
            print("Goal node found ")
            break

        visited.append(node)
        print(node)
        l=[]
        for j in range(i+1):

            if node in d[j]:
                for k in range(7):
                    if graph[node][k]>0 and k not in visited:
                        stack.append(k)
                        l.append(k)
                break
        if len(l) !=0 and len(d)<=j+1 and l not in d:
            d.append(l)
        elif len(d)>j+1 and len(l)!=0 and l[0] not in d[j+1]:
            d[j+1].extend(l)


if f == 0 :
    print("Cannot find the goal node")