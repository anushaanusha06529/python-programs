num=9876543211
res=0
while num!=0:
    ld=num%10
    if ld%2==0:
        res+=ld
    num//=10
print(res)
    
