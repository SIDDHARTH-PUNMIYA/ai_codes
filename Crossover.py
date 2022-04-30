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

val=float(input("Enter the CrossOver Probability"))
s=int(val*n)
print("\nThe Selected Samples are ")
ind=[]
l=[]
print("S={}".format(s))
cnt=0
while cnt!=s:
    num=random.randint(0,n-1)
    if num not in ind:
        ind.append(num)
        l.append(samples[num])
        print(samples[num])
        cnt+=1

# print(l)

for i in range(0,len(l),2):
    temp=l[i][0]
    l[i][0]=l[i+1][1]
    l[i+1][1]=temp

print("\nThe Selected Samples after CrossOver are ")
print("X\tY")
for i in range(s):
    print("{}\t{}".format(l[i][0],l[i][1]))