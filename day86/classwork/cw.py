# 1) შექმენით Abstract Clasess მაგალითი
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class parrot(Animal):
    def make_sound(self):
        return "შენა ხარ @%$&# !"


animals = [Dog(), Cat(), parrot()]
for animal in animals:
    print(animal.make_sound())

# 2) შექმენით polymorphism'ის მაგალითი

class Bird:
    def fly(self):
        return "დავფრინავ მაღლა ჩემი ფრთებით!"

class Airplane:
    def fly(self):
        return "დავფრინავ მაღლა ჩემი ძრავებით!"

class Kite:
    def fly(self):
        return "მაღლა დავფრინავ ზლიერი ქარით!"

flying_objects = [Bird(), Airplane(), Kite()]
for obj in flying_objects:
    print(obj.fly())

# 3) ახსენით როგორ მუშაობს თითოეული მათგანი

# Abstract Clasess ---- უზრუნველყოფს, რომ ყველა მემკვიდრე კლასმა განახორციელოს აუცილებელი მეთოდები.
# ეს ქმნის ერთგვაროვან სტრუქტურას.
# polymorphism ---- საშუალებას გვაძლევს, ერთნაირი მეთოდის სახელით (მაგ : fly)
# გამოვიძახოთ სხვადასხვა კლასის ობიექტების უნიკალური ქცევა.

# 4) გააკეთეთ აგრეგაციის მაგალითი

