graph=[[0,4,3,0,0,0,0],
       [0,0,0,0,12,5,0],
       [0,0,0,7,10,0,0],
       [0,0,0,0,2,0,0],
       [0,0,0,0,0,0,5],
       [0,0,0,0,0,0,16],
       [0,0,0,0,0,0,0]]

n=len(graph)
hVal=[14,12,11,6,4,11,0]
s=int(input("Enter the Start node "))
g=int(input("Enter the Goal Node "))

visited=[]
l=[]
l.append(s)
c=0
flag=0

print("The Path is ")
while (g not in visited):
    flag=0
    node=l.pop(0)
    print(node)
    min=10000
    ind=-1
    visited.append(node)
    if node==g:
        print("\nGoal Node Found With an Cost  of {}".format(c))
        break
    for i in range (n):
        if graph[node][i]>0:
            if min>hVal[i]:
                min=hVal[i]
                ind=i
    if ind==-1:
        flag=1
        break
    c = c + graph[node][ind]
    l.append(ind)

if flag==1:
    print("\nDead End No such Node Found")