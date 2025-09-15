
#15/09/2025
#rotation matrix

'''m=[]
n=3
for _ in range(n):
    l=list(map(int, input().split()))
    m.append(l)
for i in range(n):
    for j in range(n-1,-1,-1):
        print(m[j][i],end=" ")
    print()

           #or
m=[]
n=3
for _ in range(n):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(n):
    for j in range(n):
        print(m[n-j-1][i],end=" ")
    print()
'''
#rectangle hollow pattern
'''n=5
m=4
for i in range(1,n+1):
    for j in range(1,m+1):
        if   j==1 or j==m or i==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#hollow dimond
'''n=5
for i in range(1,n):
    s=" "*(n-i)
    if i==1:
        print(s+"* "*i)
    else:
        print(s+"* "+"  "*(i-2)+"*")
for i in range(n,0,-1):
    s=" "*(n-i)
    if i==1:
        print(s+"* "*i)
    else:
        print(s+"* "+"  "*(i-2)+"*")'''



