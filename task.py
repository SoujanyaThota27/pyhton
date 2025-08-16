# CREAT 5 VARIABLES USING DIFFERENT NAMING CONVENTION (snake_case,camelCase,PascalCase,etc...)
'''UPPER CASE--->COLLEGENAME='vgse'
LOWER CASE--->collegename='vgse'
PASCAL CASE-->Collegename="vgse"
CAMEL CASE--->collegeName="vgse"
SNAKE CASE--->college_name="vgse"
kebab case--->college-name="vgse"'''


# Try creating invalid variable names and observe the errors.
'''1a=8
print(1a) # cannot start with a numebr

$=4
print($) #cannot start with special charavter like @,$...

if a=5
print(a) #cannot use keywords like if,else etc..

a=9
print(A) #it is case sensitive even though same variable but different meaning'''



# creat one variable of each type :int,float,str,bool. print their type and id().
'''a=231
print((a),type(a),id(a))

a=231.5
print((a),type(a),id(a))

a='soujanya'
print((a),type(a),id(a))

a=True
print((a),type(a),id(a))'''

## intermediate task (manipulation & conversion)
#1.list practice:
#players=["rohit","virat","gill","dhoni"]
#-Replace "gill" with "surya".
#-Add "jadeja" at the end.
#-Print the length and second last player.

'''players=["rohit","virat","gill","dhoni"]
players[2]="surya"
players.append("jadeja")
print(players)
print(len(players))
print(players[-2])'''


#2.tupple practice.
#laptop_info=("HP","16GB","512GB SSD",2024,True)
#-try modifying one value
# -explain the result
# -acces and print the last 2 elements.

'''laptop_info=("HP","16GB","512GB SSD",2024,True)
#print(laptop_info[0])="dp"
#it is immutable we cannot change the element in tupple
print((laptop_info[-2]))
print((laptop_info[-1]))'''

##3.set practice.
#countries={"India","USA","India","Canada","UK","USA"}
#-print the set(observe duplicate).
#-add "germeny",remove "uk".

'''countries={"India","USA","India","Canada","UK","USA"}
print(countries)
countries.remove("UK")
print(countries)
countries.add("germany")
print(countries)'''


#4.frozenset pratice:
#frozen_marks=frozenset([90,85,75,85])
#-try to add or remove the value and observe the error
#-print its type.


'''frozen_marks=frozenset([90,85,75,85])
#frozen_marks.remove (frozenset(90))
print(frozen_marks)#we cannot add or remove in frozenset
print(type(frozen_marks))'''


##Advanced tasks (nesting & real-time)
#1.dictionaries
#car_info={
#    "Brand":"Tesla",
 #   "model":"model s",
 #   "price":"1.5cr",
 #   "features":["autopilot","Electric","sunroof"]
#}
#-add "color":"white"
#-update "price" to "1.7cr"
#-add nested key "insurance" with {"provide":"HDFC","valid_till":"2026"}.

'''car_info={
        "Brand":"Tesla",
        "model":"model s",
        "price":"1.5cr",
        "features":["autopilot","Electric","sunroof"]
         }
car_info["color"]="white"
print(car_info)
car_info["price"]="1.7cr"
print(car_info)
car_info["insurance"]={"provide":"HDFC","valid_till":"2026"}
print(car_info)'''


##list of disctionaries:
#books=[{"tittle":"automic habits","author":"james clear"},
#       {"tittle":"ikigai","author":"hector garcia"},
#       {"tittle":"zero to one","author":"peter thiel"}
#      ]
#-add a new book.
#-find and print tittle of the book by "peter thiel".


'''books=[{"tittle":"automic habits","author":"james clear"},
       {"tittle":"ikigai","author":"hector garcia"},
       {"tittle":"zero to one","author":"peter thiel"}
      ]
books.append({"tittle":"good omens","author":"neilgaiman"})
print(books)
#print((books{"tittle"}))--->not done the answer'''


#nested dictionary print
#laptop={"brand":"apple",
#"specs":{"ram":"16GB","storage":"1TB SSD","chip":"M2"},
#"price":"2L"
#  }
#-print "chip" value
#-print:Apple laptop comes with M2 chip and cost 2L.

'''laptop={"brand":"apple",
        "specs":{"ram":"16GB","storage":"1TB SSD","chip":"M2"},
        "price":"2L"
        }
print(laptop["specs"]["chip"])
print("Apple laptop comes with M2 chip and cost 2L")'''


#CHALLANGE TASK 
#2.Memory check:
#-assign the same valueb to 2 variables.
#-print their id()-are they same.

'''a=20
b=20
print(id(a),id(b))'''


#1.Movie tracker:
#ott_data=1[{"platform":"netflix","shows";["stranger things","wednesday"]},
#           {"platform":"prime","shows":["mirzapur","farzi"]},
#           {"platform":"hostar","shows":["special ops","the freelancer"]}
#          ]
#-add ne show to prime.
#-print all shows in netflix.


'''ott_data=[
           {"platform":"netflix","shows":["stranger things","wednesday"]},
           {"platform":"prime","shows":["mirzapur","farzi"]},
           {"platform":"hostar","shows":["special ops","the freelancer"]}
         ]
ott_data["platform":"prime"].append["shows"]="mirzapur2"
print(ott_data)'''





 










