# 2) შექმენით 10 ელემენტიანი list'ი და კომენტარის სახით დანომრეთ (მიუწერეთ ინდექსები). შემდეგ კი უბრალოდ გამოიტანეთ ეკრანზე.

number = ['one', 'tow', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','ten',]


# 3) პირველ დავალებაში შექმნილი List'იდან გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 დადებითი ინდექსებით. (slicing)
test1 = number [:3], number [7:10], number [3:6]
print(test1)

# 4) პირველ დავალებაში შექმნილი List'იდან გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 უარყოფითი ინდექსებით. (slicing)

test2 = number [2::-1], number [:7:-1], number [6:2:-1]
print(test2)

# 5) შექმენით სტრინგი და შეატრიალეთ მისი სიმბოლოები ანუ თუ თავიდან იქნებოდა "Hello" გახდეს "olleH"

name = "hallo"
test3 = name [::-1]
print(test3)