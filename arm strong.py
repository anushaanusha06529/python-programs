num=153
res=0
copy=num
pow=len(str(num))
while num!=0:
    ld=num%10
    res=res+ld**pow
    num//=10
if copy==res:
    print('arm strong number')
else:
    print('not arm strong number')
