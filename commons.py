'''len()->return number of elements.
syntax:len(string)| len(list) | len(tuple)

max()->return largest element.
syntax:max(string)|max(list)|max(tuple)

min()->return smallest element.
syntax:min(string)|min(list)|min(tuple)

sum()->returns sum of numeric elements.
syntax:sum(string)|sum(list)|sum(tuple)

sorted()->returns elements in ascending order as list.
syntax:sorted(string)|sorted(list)|sorted(tuple)

any()->returns True if any element is True.
syntax:any(string)|any(list)|any(tuple)

all()->retuens True if all elements are True.
syntax:all(string)|all(list)|all(tuple)

enumerator()->return index -value pairs as iterator.
syntax:enumerator(string)|enumerator(list)|enumerator(tuple)

reversed()->return reverse iterator.
syntax:element(string)|element(list)|element(tuple)
'''
#write a code to find second largest and second smallest element in a list
a=[100,10,99,9,999]
list=a[0]
list2=a[0]
for i in a:
    if i<list:
        list2=list
        list=i
    elif i<list2 and i!=list:
        list2=i
    
print(list)
print(list2)
           #or

l=[900,10,99,9,999]
min=float("inf")
for i in l:
    if i<min:
        min=i
s_min=float("inf")
for i in l:
    if i>min and i<s_min:
        s_min=i
print(s_min)