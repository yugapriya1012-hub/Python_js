n=[7,1,6,4,3]
l=len(n)

for i in range(l):
    for j in range(0,l-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)