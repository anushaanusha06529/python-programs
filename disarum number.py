num=135
res=0
copy=num
pow=len(str(num))
while num!=0:
    ld=num%10
    res=res+ld**pow
    pow-=1
    num//=10
if copy==res:
    print('disarm strong number')
else:
    print('not disarm strong number')


 '''#example for disarum number
    num=135
    =(1)^1+(3)^2+(5)^3
    =1+9+125
    =135
'''
