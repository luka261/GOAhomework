# 1) შექმენით car class, მიეცით 4 ატრიბუტი და შეუქმენით 2 ფუნქცია class'ში.
# ამ class'ისგან შექმენით 3 ობიექტი და სამივეზე გატესტეთ ყვლა ატრიბუტის გამოტანა და მეთოდები.


class Car:
    def __init__(self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        return f"The {self.color} {self.name} {self.model} is starting."

    def stop_engine(self):
        return f"The {self.color} {self.name} {self.model} is stopping."
# 2) შექმენით person class, მიეცით 3 ატრიბუტი და შეუქმენით 2 ფუნქცია class'ში.
# ამ class'ისგან შექმენით რამდენიმე ობიექტი და პირველ ორზე გატესტეთ ყვლა ატრიბუტის გამოტანა და მეთოდები. 
# ასევე შექმენით დამატებითი კლასის ცვლადი რომელიც დათვლის რამდენი ადამიანია ჯამში.
class Person:
    total_people = 0

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        Person.total_people += 1

    def greet(self):
        return f"Hello, my name is {self.name}."

    def get_age(self):
        return f"I am {self.age} years old."
# 
#   
# 3) დაწერეთ რას ეწოდება dunder method
# dunder method არი მეთოდი რომელიც იწერება ორი underline  
# 
# 
# 4) დაწერეთ რას ეწოდება instance variables
# IDK
# 
#  
# 5) დაწერეთ რას ეწოდება class variables
# IDK
# 
# 
# 6) ახსენით რა არის blueprint
# blueprint არის კლასის შაბლონი რომელიც აღწერს კლასის ატრიბუტებს და მეთოდებს
# 
# 