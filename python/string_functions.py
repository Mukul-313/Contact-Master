#               STRING FORMAATING  

# name = "mukul "
# age = 19
# print("hello" + name +" your age is " + str(age))
# #python 3
# print("hello {} your age is {}".format(name,age))
# #python 3.6
# print(f"hello {name} your age is {age}")

                # string Slicing 
                
# SYNTAX - [start argument : stop argument -1]
# lang="python"
# print(lang[0:4])

            # STRING ARGUMENT 
            
#SYNTAX - [ start argument : stop :argument : step]
# print("Python"[0:6:3])
# print("Python"[::-1]) # reverse string

                # STRING INDEXING

# language="python"
# print(language[3])

                #  STRING METHODS
                
# name="muKUl guPtA"
# #1  len() function 
# print(len(name))

# #2 lower method
# print(name.lower())

# #3 upper Method
# print(name.upper())

# #4 title method 
# print(name.title())

# #5 count method
# print(name.count("U"))

#6 Capitalized Method
# print(name.capitalize())

            #STRIP METHOD - used to remove space in string

# name="        Mukul      "
# name2="Mu    kul"
# dots="..................."
# print(name)
# print(name.lstrip()+dots) #remove left space
# print(name.rstrip()+dots) #remove right space
# print(name.strip()+dots)  #remove both space 
# print(name2.replace(" ","")+dots)

            # FIND & REPLACE METHOD 
            #REPLACE
# string = "she is beautiful and she is good dancer"
# print(string.replace("is","was"))
# print(string.replace("is","was",1)) 
# print(string.replace("is","was",2))

                #FIND 

# print(string.find("is"))
# print(string.find("is",5))
# is_pos1 = string.find("is")
# is_pos2 = string.find("is",is_pos1+1)
# print(is_pos2)

                # CENTER METHOD

#SYNTAX - string_name.center(location,"value")

# input name and add 4 star

# name=input("Enter Your Name : ")
# print(name.center(len(name)+8,"*"))


                # SPLIT METHOD

# SYNTAX string_name.split(argument) 
# Used to convert string into list 

# name = "Mukul Gupta age:20"
# print(name.split(" "))


                # EndSwith Method

#Syntax string_name.endswith("value",starting_value,ending_value)
#check string Ends with given value or not(!), return true or false

# str1="Welcome to the console!"
# print(str1.endswith("!"))
# print(str1.endswith("to",2,10))


                #ISALNUM METHOD 

# Check the given string is alpha numeric or not ((A-Z),(a-z),(0-9))
# Syntax string_name.isalnum()

# str1="Welcometotheconsole1221"
# print(str1.isalnum()) 

                # isalpha Method

# check the given string is alphabetic or not ((A-Z),(a-z)) return true 
# if string have numeric value it return false
# Syntax string_name.isalpha()

# print(str1.isalpha())

                # islower method 

# check the string have all lower values return true
# Syntax string_name.islower  

# str2="mukul gupta"
# print(str2.islower())

                # isprintable method

# The isprintable() method returns True 
# if all the values within the given string are printable, 
# if not, then return False.

# str1 = "We wish you a Merry Christmas\n"
# print(str1.isprintable())
# str1 = "We wish you a Merry Christmas"
# print(str1.isprintable())

                # isspace method

# The isspace() method returns True only and only 
# if the string contains white spaces, else returns False.

# str1 = "   mukul gupta     "       #using Spacebar
# print(str1.isspace())
# str2 = "        "       #using Tab
# print(str2.isspace())

                # istittle method

# The isspace() method returns True only and only
# if the string contains white spaces, else returns False.

# str1 = "World Health Organization" 
# print(str1.istitle())

                # isupper method

# The isupper() method returns True 
# if all the characters in the string are upper case, 
# else it returns False.

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

                # startswith method

# The startswith() method checks if the string starts with a given value. 
# If yes then return True, 
# else return False.

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

                # swapcase method

# The swapcase() method changes the character casing of the string. 
# Upper case are converted to lower case  
# and lower case to upper case

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())