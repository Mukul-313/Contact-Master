# mixed = [ 1 ,"two", 3, 4 ,5.0, 6.0, "seven", None]
# print(mixed)
# mixed[2] = "three"
# print(mixed)

#   LIST METHODS 
#1. append method - insert in last position
#2. insert(position,data) - isert at particular position
#3. list = list1+list2 
#4. extend method - used to extend items in list 
#   list.extend(list1)
#5. pop method - used to delete element in list default last item we can access item any time  
#6. delete operator - used to delete item in list
# 7. remove method - remove element in list
#8. check whether particular element is present or not 
#9. print multiple value 
#10. list iteration 
#11. Update List
#12. Count Method
#13. Sort Method
#14. Sorted function
#15. Clear Method
#16. Copy method
# 17. Split method
#18. Join method
#19. List in Loops
#20. List inside List 
#21. List with range function
#22.Index method
#23. Pass  list in function
#24. MIN & MAX function
#25. REVERSE LIST 


# fruits=['apple','banana']
# fruits1=['grapes','mango']
fruits3=['apple','mango','banana','grapes'] 
# fruits.insert(1,"guava")
# print(fruits)
# fruits2=fruits+fruits1
# t=len(fruits2)
# print(fruits2)
# fruits.extend(fruits1)
# print(fruits)
# print(fruits.pop())
# print(fruits)
# del fruits[3]
# print(fruits)
# fruits.remove('apple')
# print(fruits)
# if 'guava' in fruits:
#     print("element is present")
# else: 
#     print("element is not present")
# print(fruits3[0:4:1])
# for i in range(t):
#     print(fruits2[i]) 
# fruits[0]="mango"
# print(fruits)
# print(fruits3.count('apple'))
numbers=[1,9,5,7,3,6,8,0,2,4]
numbers.sort()
print(numbers) # SORT in Accending order 
print(numbers.sort(reverse=True)) # SORT in Deccending order
#print(sorted(numbers)) # PRINT SORT LIST WITHOUT SORTING IT
# numbers.clear()
# print(numbers) 
# numbers_copy=numbers.copy()
# print(numbers_copy)
# user_info="Mukul 06".split()
# print(user_info)
# user_info=["Mukul","06" ]
# print(' '.join(user_info))
# for fruits3 in fruits3:
#     print(fruits3)
# i = 0
# while i < len(fruits3):
#     print(fruits3[i])
#     i += 1
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0])
# print(matrix[2][0])
# for sublist in matrix:
#     for i in sublist:
#         print(i) 
# numbers=list(range(1,21))
# print(numbers)
# print(fruits3.index('mango'))
# numbers=[1,2,3,4,5,6,7,8,9]
# def negative_list(l):
#     negative=[]
#     for i in l: 
#         negative.append(-i)
#     return negative
# print(negative_list(numbers))
# print(min(numbers))
# print(max(numbers))
# def greatest_diff(l): 
#     return max(l)-min(l)
# print(greatest_diff(numbers))

print(fruits3.reverse())