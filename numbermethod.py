#1,absolute value=the absolute value of a number is its distance from zero on the numberline,without considering its sign

'''num=100
num2=-30
print(abs(num))
print(abs(num2))'''

#2.integer method
'''num=20
num2=-20.56
print(abs(int(num)))'''

#3.round method
'''ip=9.56732
print(round(ip,3))'''

#4.float method= used to convert integer value to floating value
'''num=float("inf")
print(num)'''
#1
'''num=float("inf")
list=[100,1000,10000,100000]
for i in list:
    if i>num:
        num=i
print(num)'''
#2
'''num=float("-inf")
list=[100,1000,10000,100000]
for i in list:
    if i>num:
        num=i
print(num)'''
#3
'''num=float("inf")
list=[-20,50,-30,10]
if list[0]<num:
    num=list[0]
print(num)'''

#4
'''num=float("inf")
list=[-20,30,-50,10]
for i in list:
    if i<num:
        num=i
print(abs(num))'''

#5.divmod method
'''num=2568
print(divmod(num,2))'''

#complex method
'''num=6
img_val=13
print(complex(num,img_val))'''

#type checking method                                                           1.type()                                                                       2.isinstance-->checking for boolean functions

#1.type()
'''num=50
print(type(num))'''

#2.isinstance()
'''num=[10,10.4,11,2.34,13,23.5,15]
def is_inst(i):
    return isinstance(i,int)
res=[is_inst(i) for i in num]
print(res)'''

'''num=[10,10.4,11,2.34,13,23.5,15]
def sample():
    for i in num:
        print(isinstance(i,int))
sample()'''

#math module
#1.factorial
'''import math
num=5
print(math.factorial(num))'''

#2.ceil()
'''import math
num=8.4
print(math.ceil(num))'''

#3.trunc method
'''import math
num=8.4
print(math.trunc(num))'''

'''import math
num=9.8
print(math.floor(num))'''

#float abs-->fabs
'''import math
print(math.fabs(-5.6))'''

#lcm
'''import math
num=10
num2=2
print(math.lcm(num,num2))'''

#gcd 
'''import math
num=10
num2=2
print(math.gcd(num,num2))'''

#square root
'''import math
print(math.sqrt(64))'''

#power
'''import math
print(math.pow(6,3))'''



