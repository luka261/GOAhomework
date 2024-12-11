list1 = [2, 51, 11, 13, 51, 100]
list2 = [3, 432, 46, 13, 96, 943,]

# 1. Output every item from list with positive indexing.

print(list1)


# 3. Replace the last element of a list with a new value.

list1[5] = list2[3]
print(list1)

# 4. Replace the fifth element of a list with a new value.

list1[4] = list2[5]

print(list1)


# 2. Output every item from list with negative indexing.

list1 = list1[::-1]
print(list1)