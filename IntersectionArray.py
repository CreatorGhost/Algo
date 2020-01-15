'''

'''


a=[1,3,7]
b=[1,2,4,5,7]
d=[]
c=0
i,j=0,0
while i < len(a) and j < len(b):
    c=c+1
    if a[i] < b[j]:
        i+=1
    elif a[i]>b[j]:
        j+=1
    
    elif a[i] == b[j]:
        
        d.append(a[i])
        i+=1
        j=j+1


print("Common element are:")
print(d)
