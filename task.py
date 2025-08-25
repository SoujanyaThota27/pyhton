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


#creat a list of factorial of first 5 number using list comprehensions

'''import math
factorial=[math.factorial(i) for i in range(1,6)]
print(factorial)'''

