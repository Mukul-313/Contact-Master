#1. ENUMERATION FUNCTION 

# names=['mukul','mridul','rahul']

# def func(l,s):
#     for pos,name in enumerate(l):
#         if name==s:
#             return pos
#     return -1

# print(func(names,'rahul'))


# pos =0 
# for name in names:
#     print(f"{pos} ----> {name}")
#     pos +=1 

# #with enumeration 

# for pos, name in enumerate(names): 
#      print(f"{pos} ----> {name}")

#2. MAP FUNCTION 

# numbers=[1,2,3,4]

# s=list(map(lambda a:a**2,numbers)) 
# print(s)


#3. FILTER FUNCTION

# numbers=list(range(1,11))
# print(numbers)
# even=tuple(filter(lambda a: a%2==0, numbers))
# print(even)

#4. ZIP FUNCTION 

# user_id=['user1','user2','user3']
# names=['mukul','rahul','mridul']
# last_name=['gupta','kushwah','kumar']
# print(dict(zip(user_id,names)))
# print(list(zip(user_id,names,last_name)))


# def average_finder(*args):
#    average=[]
#    for pair in zip(*args):
#       average.append(sum(pair)/len(pair))
#    return average
# average_finder=lambda *args:[sum(pair)/len(pair)for pair in zip (*args)]

# print(average_finder([1,2,3,],[4,5,6],[1,2,3]))

#5. ANY ALL FUNCTION

# numbers=[2,4,6,8,10]
# numbers1=[1,3,5,7,9,2]
# print(all([num%2==0 for num in numbers]))
# print(any([num%2==0 for num in numbers1]))

#6. MIN & MAX FUNCTION 

# names=['Mukul','rahul','abc','a']
# print(max(names,key=lambda item:len(item)))
# print(min(names,key=lambda item:len(item)))

#7.  SORTED FUNCTION

# guitars=[ 
#     {'model':'yamaha f310','price':8400},
#      {'model':'faith naptune','price':50000},
#       {'model':'faith apollo venus','price':35000},
#        {'model':'taylor 814ce','price':450000}
# ]
# print(sorted(guitars,key=lambda d:d['price']))
# print("     ")
# print(sorted(guitars,key=lambda d:d['price'],reverse=True))

#8. DOC STRING

# def add (a,b):
#     '''this function takes 2 numbers and return their value'''
#     return a+b

# print(add.__doc__)