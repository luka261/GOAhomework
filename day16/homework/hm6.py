




# 2) გამოიყენეთ for loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი
for y in range (11):
    print(y)
    y = y + 1
# 3) გამოიყენეთ while loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი
x = 0
while x <= 10 :
    print(x)
    x = x + 1
# 4) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით ლუწია თუ კენტი. (hints:       10 % 2 = 0;        5 % 2 = 1)

def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."


user_input = input("Please enter a number: ")


try:
    number = int(user_input)
    result = check_even_odd(number)
    print(result)
except ValueError:
    print("That's not a valid number!")


# 5) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade ამ ფოტოს მიხედვით: 
# (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)


def check_grade_scores(score):
    if 90 <= score <= 100:
        return "You got an A, you nerd!"
    elif 80 <= score <= 89:
        return "You got a B, you Asian!"
    elif 60 <= score <= 79:
        return "You got a C, you average!"
    elif 40 <= score <= 59:
        return "You got a D, you disappointment!"
    elif 0 <= score <= 39:
        return "You got an F, you failure!"
    else:
        return "Invalid score enter a score between 0 and 100 you idiot"

user_input = input("Please enter your score: ")

try:
    score = int(user_input)
    result = check_grade_scores(score)
    print(result)
except ValueError:
    print("That's not a valid number!")
