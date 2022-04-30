n=int(input("Enter the number of nodes in the Graph "))
path=[]
hold=[]
explored=[]
parents=[]
HeuristicValue=[]
prevParents=[]
graph=[[0,4,3,0,0,0,0],
       [0,0,0,0,12,5,0],
       [0,0,0,7,10,0,0],
       [0,0,0,0,2,0,0],
       [0,0,0,0,0,0,5],
       [0,0,0,0,0,0,16],
       [0,0,0,0,0,0,0]]
hVal=[14,12,11,6,4,11,0]

for i in range (n):
    hold.append(10000)
    parents.append([-1])
    prevParents.append(0)
    HeuristicValue.append(10000)

#### For Dynamic Graph Input #####
# graph=[]
# hVal=[]
# print("Enter the Hueristic Values")
# numbers = [int(i) for i in input().split(" ")]
# hVal.append(num for num in numbers)
# hVal.pop()
# print(hVal)
#
# for i in range(0,n):
#     numbers=[]
#     print("Enter the node costs for Node {} ".format(i))
#     numbers = [int(i) for i in input().split(" ")]
#     graph.append(numbers)

print(graph)

sNode=int(input("Enter the starting Node "))
gNode=int(input("Enter the Goal Node "))

ptr=sNode
ptrVal=0
ptrValH=0
while (gNode not in explored) :
    # prevPtrValH = ptrValH
    prevPtr = ptr
    print("Current Exploration Node {}".format(ptr))
    cNodes=[]
    h_val=[]
    dist=[]
    for i in range(0,n):
        if graph[ptr][i]>0:
            cNodes.append(i)
            h_val.append(hVal[i])
    for i in range(len(cNodes)):
        parents[cNodes[i]].append(ptr)
        dist.append(graph[ptr][cNodes[i]]+h_val[i])
        if (ptrVal+graph[ptr][cNodes[i]]+h_val[i]) < (hold[cNodes[i]]):
            hold[cNodes[i]] = ptrVal + graph[ptr][cNodes[i]]+ h_val[i]
            if(HeuristicValue[cNodes[i]]>ptrVal + graph[ptr][cNodes[i]]+ h_val[i]):
                HeuristicValue[cNodes[i]]=ptrVal + graph[ptr][cNodes[i]]+ h_val[i]

    # if gNode in explored:
    #     path.append(ptr)
    #     break

    if len(dist)==0:
        for i in range(n):
            if hold[i]!=10000:
                ptr=i
                ptrValH=hold[i]
                ptrVal=hold[i]-hVal[i]
    else:
        min_ind=dist.index(min(dist))
        ptrVal=ptrVal+graph[ptr][cNodes[min_ind]]
        ptrValH=ptrVal+hVal[cNodes[min_ind]]
        ptr = cNodes[min_ind]

    # print(ptr)
    print("PTR VAl H = {}".format(ptrValH))
    sptr=ptr
    val=hold[ptr]
    hold[ptr]=10000
    #print(" Holding = {} ".format(hold))
    ind=hold.index(min(hold))
    #print("Min hold index {}".format(ind))
    print("Explored = {} ".format(explored))
    #print(" Holding = {} ".format(hold))
    if ptrValH>hold[ind] and (ind not in explored):
        if(hold[ptr]>ptrValH):
            hold[ptr]=ptrValH
        ptr=ind
        ptrVal=hold[ind]-hVal[ind]
        hold[ptr]=10000
    if ptr!=sptr:
        if(hold[sptr]>val):
            hold[sptr]=val
    prevParents[ptr]=prevPtr
    print(" Holding = {} ".format(hold))
    explored.append(ptr)
    print("Ptr Val dist = {}\n".format(ptrVal))
    path.append(ptr)

# print(parents)
# print(HeuristicValue)
distValue=[]
for i in range(n):
    if(HeuristicValue[i] !=10000 ):
        distValue.append(HeuristicValue[i]-hVal[i] )
    else:
        distValue.append(0)
# print(distValue)
# print(parents[gNode][-1])
realpath=[]

ptr=gNode
i=0
while(ptr!=sNode):
    allParent=parents[ptr][1:(len(parents[ptr]))]
    # print(ptr)
    # print(allParent)
    for p in allParent:
        if distValue[p]+graph[p][ptr]==distValue[ptr]:
            realpath.append(ptr)
            ptr=p

# print(realpath)


print("************ The PATH IS ***************")
print("{} -> ".format(sNode),end="")
l=len(realpath)
for i in range(len(realpath)-1):
    print("{} -> ".format(realpath[l-i-1]),end="")
print("{} ".format(gNode),end="")
print('\n\n')
print("************ The Exploration of Nodes is in order ***************")
print("{} -> ".format(sNode),end="")
for i in range(len(path)-2):
    print("{} -> ".format(path[i]),end="")
print("{} -> {}".format(path[len(path)-2],gNode),end=" ")

print("\nThe cost to reach Goal Node {} from {} is {}".format(gNode,sNode,distValue[gNode]))

