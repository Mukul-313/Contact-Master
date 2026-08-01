#ARGS( *)

# def all_total(*args):
#     print(args)
#     print(type(args))
# all_total(1,2,3,4,5)

# def total_fun(*args):
#     total=0
#     for num in args:
#         total += num
#     return total

# print(total_fun(1,2,3,4,5,6,45))

# ARGS_with_Normal_Parameter

# def multiply(num, *args):
#     print(num)
#     print(*args)

# multiply(1,2,3,4,5,6)

# ARGS as a Argument 

# def multiply(*args):
#     print(args)
#     print(type(args))

# num=[1,2,3,4,5,6]
# multiply(*num)# Unpack List to tuple 
# print(type(num))

# KWARGS(**) Gather item as a dictionary

# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}: {v}")
   

# func(first_name='Mukul', last_name='Gupta')  

# # Dictionary Unpacking
# d={'name':'Mukul' , 'age':19}
# func(**d)

# FUNCTION WITH ALL PARAMETER 

# def func(name,*args,last_name='unknown',**kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)

# func('mukul', 1,2,3 , a=4,b=5 )   