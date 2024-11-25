num=145
copy=num
res=0
while num!=0:
    ld=num%10
    fact=1
    for val in range(1,ld+1):
        fact=fact*val
    res=res+fact
    num//=10
if copy==res:
    print('strong number')
else:
    print('not strong number')
    
