# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# # LIST COMPREHENSION

# square=[i**2 for i in range(1,11) ]
# print(square)
# negative=[-i for i in range(1,11)]
# print(negative)

# names=["mukul",'saurav','rahul']
# new_list=[name[0] for name in names]
# print(new_list)

# even=[i for i in range(1,11) if i%2==0]
# print(even)
# odd=[i for i in range(1,11) if i%2!=0]
# print(odd)

# nums=[1,2,3,4,5,6,7,8,9,10]
# new_list=[]
# for i in nums:
#     if i%2==0:
#         new_list.append(i*2)
#     else: 
#         new_list.append(-i)
# print(new_list)

# new_list2=[i*2 if(i%2==0) else -i for i in nums]
# print(new_list2)


# example=[[1,2,3],[1,2,3],[1,2,3]]
# nested_comp=[[i for i in range(1,4)] for j in range(3)]
# print(nested_comp)