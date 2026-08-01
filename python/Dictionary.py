#1. Create dictionary
#2. How to access data from dictionary
#3. IN keyword and Loops in dictionary 
#4. KEYS & VALUE Method
#5. Item method
#6. Add Data & Delete data 
#7. Update Method
#8. From Keys Method
#9. Get Method
#10. Clear & Copy Method

user={'name':'mukul',
      'fav_song':'desi kalakar',
      'fav_movie':['96','RX100'],}
# user1=dict(name='mukul',age=19)
# print(user)
# print(user1)
# print(type(user),type(user1))
# print(user['name'])
# print(user1['age'])
# print(user.get('age'))

# # check key 
# if 'name' in user:
#     print('present')
# else:
#     print('not present')

# # check value
# if 'mukul' in user:
#     print('present')
# else: 
#     print('not present')

# # check list in dictionary
# if list_name in user:
#     print('present')
# else:
#     print('not present')

# for i in user:
#     print(i)

# for i in user.values():
#     print(i)

# for i in user:
#     print(user[i])

# user_value = user.values()
# print(user_value)

# user_info=user.keys()
# print(user_info)

# user_item=user.items()
# print(user_item)

# for key,value in user.items():
#     print(key,value)

# add method
# user['fav_tune']=['song1','song2']
# print(user)

# # pop method
# popped=user.pop('fav_tune')
# print(popped)

#popitem method
# popped_item=user.popitem()
# print(popped_item)
# print(user)

# more_info=dict(state='Uttar Pradesh',skill='Coding')
# user.update(more_info)
# print(user)

# d=dict.fromkeys(['name','age','height'],'unknown')
# print(d)

# print(user.get('name'))
# print(user.get('names'))
# print(user.get('names','not found !'))

# user.clear()
# print(user)

# user1=user.copy()
# print(user1)
