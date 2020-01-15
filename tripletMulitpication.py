def triFact(a,t,s):
    l=[]
    for i in range(s,len(a)):
        f=int(t/a[i])
        l.append(a[i])
        j=len(l)-1
        while j >0:
            j-=1
            if l[j] ==f:
                print ("Two elements are ", a[i],f)
                return 1
    return 0
                
    
def mn(a,t):
    for i in range (len(a)):
        f=int(t/a[i])
        k=triFact(a,f,i)
        if k==1:
            
            return 1
    return 0
        
a=[int(x) for x in input().split()]
t=int(input())
an=mn(a,t)
print(an)
