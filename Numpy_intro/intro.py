import numpy as np
print(list(range(0,5)))
print(list(range(0,10,2))) 

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
# print(list1 * list2)

new_list = []
for i in range(0,len(list1),2):
    new_list.append(list1[i] * list2[i])
print(new_list)