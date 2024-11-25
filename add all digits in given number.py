num=2029
res=0
while num!=0:
    ld=num%10
    res=res+ld
    num//=10

print(res)    
