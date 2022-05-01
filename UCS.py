graph=[[0,7,3,0,0,0,0],
       [0,0,0,0,6,0,0],
       [0,2,0,9,0,0,0],
       [0,0,0,0,3,0,0],
       [0,0,0,0,0,2,1],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]


visited=[]
n=len(graph)
s=int(input("Enter the Start Node"))
g=int(input("Enter the Goal node Node"))
l=[1000]*n

l[s]=0
prevParents=[-1]*n

path=[]

while(g not in visited):
    d=min(l)
    node=l.index(d)
    print("Min value= {} and index ={}".format(d,node))
    if node not  in visited:
        visited.append(node)
        for i in range(n):
            if graph[node][i]>0 :
                if l[i]> d+graph[node][i]  and  i not in visited :
                    l[i]=d+graph[node][i]
                    prevParents[i]=node
        l[node]=1000
        path.append(l[:])
        print(path)


print("visited nodes order = {}".format(visited))
print("Previous Parents with optimal Costs = {}".format(prevParents))
start=g
p=[]
while(start!=s):
    p.append(start)
    start=prevParents[start]

print("\n ******* The Path is ******** \n")
print(p)
print("{} -> ".format(s),end='')
for i in range(len(p)-1,-1,-1):
    print("{} -> ".format(p[i]),end='')

print("\n\nThe Optimal Cost from {} to {} is {}".format(s,g,path[len(path)-2][g]))