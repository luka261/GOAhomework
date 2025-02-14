# 2) გააკეთეთ manual_find ფუნქცია

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
find = 7

found = False  

for num in numbers: 
    if num == find:  
        found = True
        break  

if found:
    print("the number is in the list!")
else:
    print("the number isn't in the list!")



# 3) გააკეთეთ manual_swapcase ფუნქცია

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)
