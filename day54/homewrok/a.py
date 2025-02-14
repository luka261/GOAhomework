# 2) Use the map function to double the numbers in a list: [2, 4, 6, 8, 10].

numbers = [2, 4, 6, 8, 10]
doubles = list(map(lambda x: x * 2, numbers))
print(doubles)

# 3) Write a program using map to concatenate "Hello, " to each name in a list: ["Alice", "Bob", "Charlie"].

name = ["Alice", "Bob", "Charlie"]
result = list(map(lambda x: "Hello, " + x, name))
print(result)

# 4) Use map to calculate the lengths of strings in a list: ["apple", "banana", "kiwi"].

fruits = ["apple", "banana", "kiwi"]
lengths = list(map(len, fruits))   
print(lengths)

# 5) Use the filter function to keep only positive numbers from a list: [-5, 3, -2, 7, 0, 10].

numbers = [-5, 3, -2, 7, 0, 10]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)


# 6) Write a program using filter to extract words starting with the letter "p" from a list: ["pear", "apple", "peach", "grape"].

words = ["pear", "apple", "peach", "grape"]
p_words = list(filter(lambda x: x.startswith("p"), words))
print(p_words)

# 7) Use filter to find numbers greater than 50 in a list: [10, 55, 42, 78, 65, 20].
numbers = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print(greater_than_50)


