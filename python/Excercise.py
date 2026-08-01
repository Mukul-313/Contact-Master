                # EXCERCISE 1
#print("this is \\\\ Double backslash")
#print(" these are /\/\/\/\/\/\ mountains")
#print(" \\\"  \\n \\t  \\\' ")
#print("he is \t awesome")

                #EXCERCISE 2

# num2,num1,num= input("Enter Three numbers :").split()
# print(f"Average of Three Number is : {(int(num)+int(num1)+int(num2)) / 3}")

                #EXCERCISE 3 

# name=input("enter your name:")
# print(f"Reverse Of Your Name is{name[-1::-1]}") 

                #EXCERCISE 4

# name,char=input("Enter Your Name and Character to Find comma Seprated: ").split(",")
# print(len(name))
# print(name.lower().count(char.lower()))

                #EXCERSICE 5
                # NUMBER GUESSING GAME

# win_num=43
# a=int(input("Guess a number: "))
# if a==win_num:
#     print("YOU WIN !!!")
# else:
#     if a<win_num:
#         print(" Too Low !! ")
#     else:
#         print("Too High !!!")

                #EXCERSICE 6

# name=input("Enter Your name: ")
# age=int(input("Enter Your Age: "))
# if age>=10 and (name[0]=='a' or name[0]=='A'):
#     print("You can watch COCO!!")
# else:
#     print("You can't watch COCO !!")

                #  Excersice 7  

# num=int(input("Enter a number :"))
# i=1
# total = 0
# while i<=num:
#     total+=i
# i+=1
# print(total)

                # EXCERCISE 8
# n=input("Enter number:")
# i=0
# total=0 
# while i< len(n):
#     total+=int(n[i])
#     i+=1
#     print(total)

                # EXCERCISE 9

# name = input("Enter your name : ")
# i = 0
# temp = ""
# while i<= len(name): 
#     if name[i] not in temp:
#         temp += name[i]
#         print(f"{name[i]}:{name.count(name[i])}")
#     i += 1

                #EXCERCISE 10
# import random
# win_num = random.randint(1,100)
# game_over = False
# guess = 1 
# a=int(input("Guess a number between 0 to 100 : "))

# while not game_over:
#     if a == win_num:
#         print("YOU WIN !!!")
#         print(f"You guessed this number in {guess} times")
#         game_over=True
#     else:
#         if a < win_num:
#             print(" Too Low !! ")

#         else:
#             print("Too High !!!")
#     guess += 1
#     a = int(input(" Guess again :"))

                # EXCERCISE 11

# def greater(num,num1): 
#     if num>num1:
#           return  print(f"{num} is greater than {num2}")
#     else:
#           return print(f"{num1} is greater than {num}")
    
# a,b=input("Enter two numbers : ").split()
# a=int(a)
# b=int(b)
# greater(a,b)

            # EXCERCISE 12

# def is_palindrome(pali):
#     if pali==pali[::-1]:
#         return True
#     else:
#       return  False
    
# name=input("Enter palindrone name: ")
# print(is_palindrome(name))

            #EXCERCISE 13
            # FIBONNACI SERIES
# def fibonnaci(n):
#     a=0
#     b=1
#     if n == 1:
#         print(a)
#     elif n == 2:
#          print(a,b)
#     else: 
#         print(a,b, end = " ")
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b, end = " ")

# n=int(input("Enter a number to print fibonnaci series : "))
# fibonnaci(n)

                #EXCERCISE 14
# numbers=[1,2,3,4,5]
# def square(l):
#     square_list=[]
#     for i in l:
#          square_list.append(i**2)
#     return square_list
# print(square(numbers))

                #EXCERCISE 15

# numbers=[1,2,3,4,5]
# def reverse_list(l):
#     #reverse_list=[]
#     l.reverse()
#     return l
# print(reverse_list(numbers))

                #OR

# def reverse_list(l):
#     return l[::-1]
# # print(reverse_list(numbers))

            #OR USING APPEND OR POP 
# def reverse_list(l):
#     r_list=[]
#     for i in range(len(l)):
#         pop_item=l.pop()
#         r_list.append(pop_item)
#     return(r_list)
# print(reverse_list(numbers))

                #EXCERCISE 16

# words=['apple','kiwi','mango']
# def reverse_list(l):
#     elements=[]
#     for i in l:
#         elements.append(i[::-1])
#     return elements
# print(reverse_list(words))

                #Excercise 17
# def fillter(l):
#     odd=[]
#     even=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     output=[odd,even]
#     return (output)     
# numbers=[1,2,3,4,5,6,7,8,9]
# print(fillter(numbers))         

                #EXCERCISE 18

# def cube_finder(n):
#     cubes={}
#     for i in range(1,n+1):
#         cubes[i]=i**3
#     return cubes

# print(cube_finder(10)) 

                #EXCERCISE 19

# def word_counter(s):
#     count={} 
#     for i in s:
#         count[i]=s.count(i)
#     return count

# print(word_counter('Mukul'))

                #EXCERCISE 20 

# user={}

# name=input('Enter Your name:')
# age=input('Enter your age:')
# fav_movies=input("Enter your favourite movies separated by comma:").split(',')
# fav_song=input("Enter your favourite song separated by comma:").split(',')

# user['name']=name
# user['age']=age
# user['fav_movies']=fav_movies
# user['fav_songs']=fav_song


# for key,value in user.items():
#     print(f"{key}:{value}")

                #EXCERCISE 21
# l=['Mukul','ABC','XYZ']
# def reverse_list(l):
#     new_list=[]
#     for i in l:
#         new_list.append(i[::-1])
#     return new_list
    
# print(reverse_list(l))

#    # LIST COMPREHENSION
# def reverse(l):
#    return[i[::-1] for i in l]

# print(reverse(l)) 

                #EXCERCISE 22
# def num2(l):
#     return [str(i) for i in l if (type(i) == int or type(i)==float) ]

# print(num2(["True","False",[1,2,3],1,1.0,3]))

                #EXCERCISE 23

# def power_calculate(num,*args):
#     if args:
#         return [i**num for i in args]
#     else: 
#         return "You didn't pass args"
# nums=[1,2,3]
# print(power_calculate(3,*nums))

                #EXCERCISE 24

# names=['mukul','rahul']

# def func(l,**kwargs):
#     if kwargs.get('reverse_str')==True:
#         return [name[::-1].title() for name in  l]
#     else:
#         return [name.title() for name in l]

# print(func(names,reverse_str=True))

                #EXCERCISE 25
# from functools import wraps
# import time

# def calculate_time(any_function):
#     @wraps(any_function)
#     def wrapper(*args,**kwargs):
#         t1=time.time()
#         value=any_function(*args,*kwargs)
#         t2=time.time()
#         print(t2-t1)
#         return value
#     return wrapper

# @calculate_time
# def square_finder(n):
#     return [i**2 for i in range(1,n+1)]

# print(square_finder(10))

                #EXCERCISE 26
# def even(n):
    
#     for num in range(2,n+1,2):
#             yield(num) 

# for i in even(10):
#     print(i)


                # EXCERCISE 27 Simple calculator 

# n=45
# m=6

# ans1=n+m
# print("Addition of" , n , "+" , m , "is" , ans1)
# ans1=n-m
# print("Subtraction  of" , n , "-" , m , "is" , ans1)
# ans1=n*m
# print("Multiplication  of" , n , "*" , m , "is" , ans1)
# ans1=n/m
# print("Division  of" , n , "/" , m , "is" , ans1)
# ans1=n%m
# print("Remainder of" , n , "%" , m , "is" , ans1)


                # EXCERCISE 28

# import time
# timestamp = time.strftime('%H')
# print(timestamp)
# con_timestamp=int(timestamp)
# # con_timestamp=int(input("Enter hour :  "))


# if (con_timestamp<12):
#     print("Good Morning sir ")
# elif(con_timestamp<=17):
#     print("Good Afternoon sir")
# else:
#     print("Good Evening Sir")

                # EXCERCISE 28


# Python program to display the Fibonacci sequence

# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = int(input("Enter the number to print fibonacci series : "))

# if nterms <= 0:
#     print("Plese enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     for i in range(nterms):
#         print(recur_fibo(i))

                # EXCERCISE 29

# LEAP YEAR CHECKER 

def is_leap(year):
    
    if(year % 4==0 and year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = int(input("Enter year to check whether it is leap year or not :"))
is_leap(year)