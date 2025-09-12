#strings built-in functions
#-->1.case converstion
#-->2.searching & finding methods
#-->3.triming & replacing method
#-->4.checking
#-->5.spliting and joining
#-->6.encode
'''s="a"
print(ord(s))

s="a"
print(chr(ord(s)-32))'''

#-->1.case conversion

#1.lower of function-->lower()                                              which is used to convert uppercase to lowercase

'''s="SOUJANYA"
print(s.lower())'''

#2.upper of function-->upper()                                              which is used to conver lowercase to uppercase
'''s="soujanya"
print(s.upper())'''

#3.captalize()                                                              which is used to convert lower to upper case of a string
'''s="soujanya"
print(s.capitalize())'''

#4.title()                                                                  which is used to upper case of every first char of words in a sentence
'''s="iam a python developer"
print(s.title())'''

#5.swape case()                                                              which is used to convert lower to upper and also upper to lower case in a string

'''s="sOUJANYA"
print(s.swapcase())'''

#swapcase background code---

'''def soujanya(s):
    l=len(s)
    res=" "
    for i in range(l):
        if ord(s[i])<=90:
            res+=chr(ord(s[i])+32)
        else:
            res+=chr(ord(s[i])-32)
    return res
s="AbCd"
print(soujanya(s))'''

#-->3.triming & replacing method
#strip()----                                                                function used to remove excess spaces at starting and ending of a string
'''s="     soujanya     "
print(s.strip())'''

#ls strip()------                                                        function which is used to remove excess space at starting of a strip
'''s="  soujanya    "
print(s)
print(s.lstrip()+"soujanya")'''

#rs strip()                                                                   function is used to remove excess space at ending of a strip
'''s="  soujanya    "
print(s)
print(s.rstrip()+"soujnaya")'''

#replace()-----                                                              function use to replace aspecif word or char
'''s="iam a java developer"
print(s.replace("java","python"))'''

#count()----                                                                  function is used to get count of a specific char̥ in string
'''s="iam a python developer"
print(s.count("a"))'''

'''s="a"
print(chr(ord(s))+32)'''

#zfill                                                                         To check it is fill the numbers r not                                          syntax:(s.zfill(enter a number))

'''s="2.5"
print(s.isnumeric())'''

'''s="abc"
print(s.zfill(4))'''

#ljust()
'''s="abc"
print(s.ljust(4,"_"))'''

#rjust()
'''s="abc"
print(s.rjust(4,"_"))'''
#center()
'''s="abc"
print(s.center(5,"_"))'''




#3.searching and finding methods
#find()                                                                       To find a character or a substring
'''s="soujanya patel"
print(s.find("patel"))

s="hello"
print(s.find("hell"))'''

#rfind()                                                                      To find last occurence of char or substring
'''s="hello hello hello hello"
print(s.rfind("hell"))
s="soujanyapatel soujanyapatel soujanyapatel"
print(s.rfind("sou"))
s="sam sam sam sam "
print(s.rfind("sa"))'''


# user defined function
'''def rsoujanya(s,sub):
    for i in range(len(s)-1,-1,-1):
        if s[i]==sub:
            return
s="hello hello hello"
sub="h"
print(rsoujanya(s,sub))'''

#index()                                                                      To find a index of char in a string
'''s="sahasra"
print(s.index("r"))

s="soujanya"
print(s.index("j"))'''

#checking built in function
#startswith()                                                                 To check its prefix start with sub or not(True/false)
'''s="alekya"
prefix="ale"
print(s.startswith(prefix))

s="alekya"
prefix="kya"
print(s.startswith(prefix))
'''
##endswith()                                                                 To check its suffix start with sub or not(True/false)
'''s="alekya"
suffix="ale"
print(s.endswith(suffix))

s="alekya"
suffix="kya"
print(s.endswith(suffix))'''

#islower()                                                                    To check whether it is lower case string or not
'''s="Soujanya"
print(s.islower())
s="soujanya"
print(s.islower())
'''
#isupper()                                                                    To check whether it is upper case string or not
'''s="SOUJANYA"
print(s.isupper())
s="soujanya"
print(s.isupper())'''


#isalpha()                                                                    To check whether string contains are alphabate or not----(True/false)

'''s="sou"
print(s.isalpha())#True
s="sou100"
print(s.isalpha())#False'''

#isdigit()                                                                    To check whether contains are digits or not

'''s="100"
print(s.isdigit())
s="sou100"
print(s.isalpha())'''

#isalnum()                                                                    To check all are combination of alpha and digits or not
'''s="hello he11o"
print(s.isalnum())
s="hel11o"
print(s.isalnum())'''

#istittle()                                                                   To check the string is in title or not
'''
s="Hello World"
print(s.istitle())

s="hello world"
print(s.istitle())'''

#isspace()                                                                    To check whether string contain space or not
'''s=" "
print(s.isspace())'''

#isdecimals()                                                                 To check the whether in decimal or not
'''s="6.6"
print(s.isdecimal())'''#false
'''s="123"
print(s.isdecimal())'''#true

#isnumeric()                                                                  To check the it is numeric or not

'''s="2.5"
print(s.isnumeric())'''#false

#encode() the out put is with b
'''s="python"
print(s.encode())

s="234"
print(s.encode())'''
#using user define isalnum
'''user_input="sou100"
if user_input.isalnum():
    print("yes")
else:
    print("no")'''

#using user define find

'''def finds(string,substring):
    for i in range(len(string)):
        if string[i:len(substring)]==substring:
            return i
        return 1
text="sou jan ya"
print(finds(text,"jan"))'''













