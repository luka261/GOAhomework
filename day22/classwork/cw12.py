# 1) შექმენით ფუნქცია რომელიც ტერმინალში გამოიტანს goodbye world'ს
# 2) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სახელს და გამოიტანს დამშვიდობებას
# 3) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს 2 რიცხვს და გამოიტანს მათ ჯამს
# 4) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს list'ს და გამოიტანს პირველ 3 რიცხვს

print('goodbye world ')


name = input("TELL ME YOUR NAME NOW ")
print("OK good bye " + name)

A = int(input("number_a "))
B = int(input("number_b "))
print (A + B)


def numberlist (list1):
    return list1[:3]


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
print(numberlist(number))