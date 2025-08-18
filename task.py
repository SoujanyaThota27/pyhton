
#print numbers from 100 to 0 the reverse which are divisible by 5
for x in range(100,-1,-1):
    if(x%5==0):
        print(x)

#write a function to print tables in reverse
for x in range(10,0,-1):
    print(f"3x{x}={3*x}")


#check whether given string is a palindrome or not--->using a function
def palidrome(word):
    for x in range(len(word)-4,0,-1):
        if word :
            print("is a palidrome")
        else:
            print("is not a palidrome")
palidrome("level")







