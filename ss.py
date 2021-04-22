l=list()
n=int(input("enter number of elements>>"))
print("enter the elements of list")

for i in range(n):
    l.append(int(input(">>")))

for i in range(n-1):
    pos=i
    for j in range(i+1,n):
        if l[pos]>l[j]:
            pos=j
        t=l[pos]
        l[pos]=l[i]
        l[i]=t

print(l)
#O(n^2)
