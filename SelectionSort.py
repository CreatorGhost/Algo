a=[int(x) for x  in input().split()]
for i in range(0,len(a)-1):
    mi,t,loc=a[i],a[i],i
    for j in range(i+1,len(a)):
        if mi>= a[j]:
            
            mi=a[j]
            loc=j
    a[i],a[loc]=a[loc],t
    
print(a)
