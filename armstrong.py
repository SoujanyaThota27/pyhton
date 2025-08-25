#1.check whether given num is armstrong or not?
'''n = 152
num = n
sum_of_powers = 0
digits = len(str(n))
while(n>0):
    digit = n%10
    sum_of_powers+= digit**digits
    n = n // 10
if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")'''


#using function preceeding and succeding of armstrong number
'''def armstrong(n):
    num= n
    a=n-1
    b=n+1
    sum_of_powers = 0
    digits = len(str(n))
    while(n):
          digit = n%10
          sum_of_powers+= digit**digits
          n = n // 10
    if (sum_of_powers==num):
        print(f"{num}is an Armstrong number")
    else:
        print(f"{num}is not an Armstrong number")
    if (sum_of_powers==n-1):
         print(f"{a}is an armstrong number")
    else: 
         print(f"{a}is not an armstrong number") 
    if (sum_of_powers==n+1):
         print(f"{b}is an armstrong number")
    else:
         print(f"{b}is not an armstrong number")
armstrong(153)'''