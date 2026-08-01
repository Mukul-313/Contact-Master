#           MAP FUNCTION (Takes function as arguments)

# l=[1,46,3,23,4,6]
# s=list(map(lambda a:a*a,l))
# print(type(s))
# print(s)


#           Filter Function 

# numebers=list(range(1,11))
# even=tuple(filter(lambda a:a%2==0, numebers))
# print(type(even))
# print(even)


#           Reduce Function 

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
print(type(sum))