# Hollow pattern code  using recursion

def hollow_pattern(n,i=0,j=0):
    if i==n:
        return
    if i==0 or i==n-1 or j==0 or j==n-1:
        a="*"
    else:
        a=" "
    print(a,end=" ")
    if j+1==n:
        print()
        hollow_pattern(n,i+1,0)
    else:
        hollow_pattern(n,i,j+1)
n=5
hollow_pattern(n)

#factorial code using recursion
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
n=5
print(fact(n))