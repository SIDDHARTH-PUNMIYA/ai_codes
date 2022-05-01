graph=[[0,4,3,0,0,0,0],
       [0,0,0,0,12,5,0],
       [0,0,0,7,10,0,0],
       [0,0,0,0,2,0,0],
       [0,0,0,0,0,0,5],
       [0,0,0,0,0,0,16],
       [0,0,0,0,0,0,0]]
hVal=[14,12,11,6,4,11,0]

n=int(input("Enter the number of nodes in the Graph "))
s=int(input("Enter the starting Node "))
g=int(input("Enter the Goal Node "))

cNode=s
hold=[10000]*n
hold[s]=0
visited=[]
p=[-1]*n
hVal[s]=0
flag=-1
cost=-1
while cNode!=g:
    val=min(hold)
    if val==10000:
        print("No more nodes Reachable")
        break
    cNode=hold.index(val)
    if cNode==g:
        flag=0
        print("\n\n****** Explored {} with cost of {} *******\n".format(g,hold[g]-hVal[g]))
        cost=hold[g]-hVal[g]
        break
    print("Exploring {}".format(cNode))
    visited.append(cNode)
    hold[cNode]=10000
    for i in range(n):
        if graph[cNode][i]>0:
            if i not in visited and hold[i]>val-hVal[cNode]+graph[cNode][i]+hVal[i]:
                hold[i]=val-hVal[cNode]+graph[cNode][i]+hVal[i]
                p[i]=cNode
    # print(p)
    print(hold)

if flag==0:
    print("The Optimal Path to Reach from {} to {} with cost {}".format(s,g,cost))
    print('')
    l=[]
    l.append(g)
    node=g
    while node!=-1:
        l.append(p[node])
        node=p[node]
    for i in range(len(l)-2,-1,-1):
        print("{} -> ".format(l[i]),end=" ")