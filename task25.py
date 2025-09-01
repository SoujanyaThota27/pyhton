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
#Create a list of factorials of the first 5 numbers using list comprehensions.
'''def factorial(num):
    return 1 if num==0 else num*factorial(num-1)
op=[factorial(i) for i in range(1,6)]
print(op)'''

