#dictionary built in functions                                                In dictionary keys are immutable values are miuatble  

#get()                                                                        To get value of particular key
#syntax:-->dict_name.get(key)                                              -->dict_name.get(key,default_value)    
'''d={"name":"soujanya","age":22,"gender":"female"}
print(d.get("name"))
print(d.get("college name"))
print(d.get("college name","not avaliable"))
print(d.get("gender","not available"))'''

'''d={"name":"soujanya","age":22,"gender":"female"}
for i in d:
    print(d[i],i)'''

#keys()-->  To get key of a dict
#syntax:-->dict_name.keys()
'''d={"name":"soujanya","age":22,"gender":"female"}
print(d.keys())'''

'''d={"name":"soujanya","age":22,"gender":"female"}
print(list(d.keys()))'''

#values()-->To get all values of a dict
#syntax:-->dict_name.values()

'''d={"name":"soujanya","age":22,"gender":"female"}
print(list(d.values()))'''

#items()-->To get key,values paier of dict(tuple)
#syntax:-->dict_name.items()
'''d={"name":"soujanya","age":22,"gender":"female"}
print(list(d.items()))'''

#update()-->To add a pair to a dictiponary
#syntax:-->dict_name({key:value})
'''d={"name":"soujanya","age":22,"gender":"female"}
d.update({"clg":"vgse"})
print(d)'''

#clear()-->To del all pairs from a dict
#syntax:-->dict_name.clear()

'''d={"name":"soujanya","age":22,"gender":"female"}
print(d.clear())'''

#copy()-->To copy to another variable.
#syntax:var_name=dict_name.copy()
'''d={"name":"soujanya","age":22,"gender":"female"}
print(d.copy())'''

#pop()-->To remove particular key value pairs
#syntax:dict_name.pop(key)-->dict_nmae.pop(key,"default value")

'''d={"name":"soujanya","age":22,"gender":"female"}
d.pop("age","not found")
print(d)'''

#fromkeys()-->To conver list element as key in a dict
#syntax:dict_name from keys(list_name,0)

l=["name","age","gender"]
d=dict.fromkeys(l,0)
print(d)

#popitem()-->To remove last update key value pair
#syntax:-->dict_nmae.popitem()

'''d={"name":"soujanya","age":22,"gender":"female"}
d.popitem()
print(d)'''

#delet()-->To remove particular key value pair nd to del entire dictionary
#syntax() del dict_name[key]   -->del dict_name
'''d={"name":"soujanya","age":22,"gender":"female"}
del d["name"]
print(d)'''

#zip()-->To conver 2 list in to dictionary
#syntax:-->d=dict(zip(key,values))
'''keys=["name","age","gender"]
values=["saha",22,"female"]
d=dict(zip(keys,values))
print(d)
'''






