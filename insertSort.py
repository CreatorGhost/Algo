a=[int(x) for x in input().split()]

for i in range(1,len(a)):
    t=a[i]
    j=i-1
    while j>=0:
        if t< a[j]:
            a[j+1]=a[j]
           
        if t>a[j]:
            break
        j-=1
    a[j+1]=t
    
print(a)
 
