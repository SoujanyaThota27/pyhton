# RULES OF FUNCTIONS-->
#reuse of block of code/statement
#avoid code repitition
#organize the code
#Need to caal/invoke the function to executes



#PROGRAMS
#static function
'''def sample():
    print("hello")
sample()'''

#dynamic-->without return statement

'''def dynamicfun(name):
    print(f"hello{name}")
dynamicfun("abhi")
dynamicfun("sou")'''

#dynamic--->with return statement

'''def theatre(mve):
    print(f"now showing {mve}")
    return("thank you-visit again")
#theatre("kingdom")
#theatre("hhmv")
print(theatre("kingdom"))
print(theatre("hhmv"))'''

'''def theatre(mve):
    print(f"now showing {mve}")
    return("thank you-visit again")
x=theatre("kingdom")
print(x)'''

# Q:(addition of 2 number)*(subtract of 2 numbers)

'''def add(a,b):
    sum=a+b
    return sum
def sub(a,b):
    sub=a-b
    return sub
x=add(12,7)
y=sub(12,7)
a=x*y
print(a)'''

#prctise all types of function syntaxes and simple examples in a doc..

#types of functions
#1.user define non parameter function

'''def add()
    #block of code
add()'''

'''def add():
    a=10
    b=12
    print(a+b)
add()'''

#user define parameter function

'''def add(parameter):# parameters is variable like a,b
    #block of code
add(values)'''

'''def sub(a,b):
    print(a-b)
sub(20,10)
sub(20,10)
sub(100,20)'''

#3. keyword arguments
'''def details(keywords):
    #block of code
details(keyword="value")'''

'''def details(vilage,HNo):
    print(vilage)
    print(HNo)
details(vilage="kdpl",HNo=11_7)'''

#4.*arguments
'''def add(*args):# or def add(*a):
    #block of code
add(values or strings)'''

'''def add(*args):
    print(sum(args))
add(1,2,3,4,5,56,67,56)'''

#5.**arguments (keyword arguments)

'''def details(**a):
    print(a)
details(------)'''



'''def details(**args):# or def details(**a):
    print(args)
details(name="suji",pin=231,city="knr")'''

#default arguments
'''def function_name():
    #block of code
function_name()'''


'''def details(name,city,batch=67):
    print(f"hello iam {name} from {city} and my batch is {batch} ")
details("sou","knr")'''


#lambda functions
 
'''x=lambda:print("hii iam soujanya")
x()'''

'''x=lambda:"hii"
print(x())'''

'''x=lambda a:a+8
print(x(2))'''

'''x=lambda a,b:a+b
print(x(2,10))'''



