import random

n=int(input("Enter the Number of Samples "))
samples=[]
for i in range(n):
    x=int(input("Enter the value of X "))
    y=int(input("Enter the value of Y "))
    samples.append([x,y])

print("The Samples are")
print("X\tY")
for i in range(n):
    print("{}\t{}".format(samples[i][0],samples[i][1]))

val=float(input("Enter the Mutation Probability"))
s=int(val*n*2)
ind=[]
x1=int(input("Enter the Max value of X "))
y1=int(input("Enter the Max value of Y "))
print("\nThe Selected Genes for Mutation are ")
cnt=0
l=[]
while cnt!=s:
    num=random.randint(0,n*2-1)
    if num not in ind:
        cnt+=1
        print("Gene Number = {} ".format(num+1))
        ind.append(num)
        l.append(num//2)
        if num%2==0:
            samples[num//2][0]=x1-samples[num//2][0]
        else:
            samples[num // 2][1] =y1 - samples[num // 2][1]


print("The Genes After Mutation Are ")
print("X\tY")
for i in range(n):
    print("{}\t{}".format(samples[i][0],samples[i][1]),end='')
    if i in l:
        print("\t[Mutated]",end='')
    print('')