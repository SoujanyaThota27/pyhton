'''n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()'''


#single loop
'''n=5
for i in range(n):
    print("*"*n)'''

'''n=5
for i in range(n):
    for _ in range(i+1):
        print(" ",end=" ")
    for _ in range(i,n):
        print("*",end=" ")
    print()'''

'''n=5
for i in range(n):
    for _ in range(i,n):
        print("*",end=" ")
    for _ in range(i+1):
        print(" ",end=" ")
    print()'''

'''n=5
for i in range(n,-1,-1):
    for j in range(i,n):
        print("*",end="")
    print()'''


#Centered pyramid pattern
'''n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")    
    print()
    '''
'''n=6
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")    
    print()'''
    
#diamond pattern
'''n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")    
    print("")
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")    
    print("")'''
    
#Right aligned half diamond
'''n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")    
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")    
    print()'''
    
#left aligned half diamond    
'''n=6
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")    
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")    
    print()'''





