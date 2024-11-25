num=24
res=0
pos=1
while num!=0:
    ld=num%2
    res=res+ld*pos
    num//=2
    pos*=10
print(res)    
