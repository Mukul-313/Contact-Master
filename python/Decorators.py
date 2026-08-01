# FUNCTION AS PARAMETER 

# l=[1,2,3,4,5]
# def my_map(func,l):
#     new_list=[]
#     for item in l: 
#         new_list.append(func(item))
#     return new_list

# print(my_map(lambda a : a**3 ,l))

# FUNCTION IN FUNCTION 

# def outer_func():
#     def inner_func():
#         print('Inside inner func')
#     return inner_func

# var = outer_func()
# var()

#  DECORATOR FUNCTION 

# from functools import wraps
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs): 
#         '''This Is decorator function'''
#         print('This is awesome function')
#         return any_function(*args,**kwargs)
#     return wrapper_function

# @decorator_function
# def func(): 
#     print('This is function ')

# func()

# def func1(a):
#     print(f'This is function with argument {a}')

# func1(4)

# @decorator_function
# def add(a,b):
#     '''This is add function'''
#     return a+b
# print(add(2,3))

# print(add.__doc__)
# print(add.__name__)

# from functools import wraps
# def only_data_type_allow(data_type):
#     def decorator(function):
#         @wraps(function)
#         def wrapper(*args,**kwags):
#             if all([type(args)==data_type for arg in args]):
#                 return function(*args,**kwags)
#             print("Invalid arguments")
#         return wrapper 
#     return decorator 

# @only_data_type_allow(str)
# def string_join(*args):
#     string = ''
#     for i in args:
#         string += i   
#     return string

# print(string_join("mukul","gupta"))