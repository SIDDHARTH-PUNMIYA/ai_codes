mat=[[1,2,3,4],
       [5,6,7,8],
       [10,10,9,9],
       [10,12,9,16]]


print("The Matrix Is")
for i in range(len(mat)):
    print(mat[i])

x=int(input("Enter the Starting X Cordinate"))
y=int(input("Enter the Starting Y Cordinate"))

cVal=mat[x][y]
pVal=-10000
flag=0

while cVal>pVal:
    flag=-1
    print("Current Value = {}".format(cVal))
    pVal=cVal
    max=cVal
    if x+1<len(mat) and max<mat[x+1][y]:
        cVal=mat[x+1][y]
        max=mat[x + 1][y]
        flag=0
    if x-1>=0 and max<mat[x-1][y]:
        cVal=mat[x-1][y]
        max=mat[x - 1][y]
        flag=1
    if y+1<len(mat[0]) and max<mat[x][y+1]:
        cVal=mat[x][y+1]
        max=mat[x][y+1]
        flag=2
    if y-1>=0 and max<mat[x][y-1]:
        cVal=mat[x][y-1]
        max=mat[x][y-1]
        flag=3

    if flag==0:
        x=x+1
    elif flag==1:
        x=x-1
    elif flag==2:
        y=y+1
    elif flag==3:
        y=y-1

    cVal=max

print("The Max Value using Hill Climbing is {}".format(max))