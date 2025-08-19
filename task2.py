#1.I/p:-
    #l1=[Sravan,harish,aravind,akhil]
    #l2=[24,17,20,18]

'''l1=["Sravan","harish","aravind","akhil"]
l2=[24,17,20,18]
for i in range(len(l1)):
    if l2[i]>=18:
        print(l1[i],"-",l2[i],"_","elgible")
    else:
        print(l1[i],"-",l2[i],"_","not elgible")'''

#2.sum of digits--->n=123 and n=120

'''n=123
res=0
while n>0:
    r=n%10
    res+=r
    n=n//10
print(res)

n=120
res=0
while n>0:
    r=n%10
    res+=r
    n=n//10
print(res)'''


#3.highest digit in an integer--->i/p n=123498

'''n=123498
res=-1
while n>0:
    r=n%10
    if r>=res:
        res=r
    n=n//10
print(res)'''


#4. choc_price=1
    #3wrappers=1choc
    #amount=21
    #how many chocs i can eat=?

'''a=21
c=a
w=a
while w>=3:
    extra_choc=w//3
    c+=extra_choc
    w=extra_choc+w%3
print(c)'''




