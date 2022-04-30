import  random
n=int(input("Enter the Number of Samples "))
samples=[]
for i in range(n):
    x=int(input("Enter the value of X "))
    y=int(input("Enter the value of Y "))
    samples.append([x,y])

print("The Original Samples are")
print("X\tY")
for i in range(n):
    print("{}\t{}".format(samples[i][0],samples[i][1]))

s=int(input("Enter the Number of Samples to be Selected"))
print("The Selected Samples are ")
for i in range(s):
    num=random.randint(0,n-1)
    print(samples[num])