# 1) შექმენით ფუნქცია multiply რომელიც მიიღებს 2 პარამეტრს (a, b) შემდეგ კი დააბრუნებს მათ ნამრავლს

def multiply_numbers():
  user_input0 = int(input("Please enter number a: "))
  user_input1 = int(input("Please enter number b: "))
  return user_input0 * user_input1

result = multiply_numbers()
print("The product of the numbers is:", result)

# 2) შექმენით ფუნქცია even_or_odd რომელიც მიიღებს რიცხვს პარამეტრად და დააბრუნებს "Even" თუ ის არის ლუწი, ხოლო "Odd" თუ კენტია


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