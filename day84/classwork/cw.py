# 1) გააკეთეთ multiple და multilevel inheritanceის მაგალითი ზუსტად ისე როგორც კლასში გავაკეთეთ ოღონდ ადამიანებზე

# cheatsheet:
# Human

# Programmer(Human)
# Designer(Human)

# Goaprogrammer(Programmer)
# Goadesiner(Designer)

# Professional(Programmer, Designer)

class Human:
    def __init__(self, name):  
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def walk(self):
        print(f"{self.name} is walking.")


class Programmer(Human):
    def code(self):
        print(f"{self.name} is coding.")


class Designer(Human):
    def make_design(self):
        print(f"{self.name} is making design.")


class Goaprogrammer(Programmer):
    def become_leader(self):
        print(f"{self.name} became leader.")


class Goadesigner(Designer):
    def create_goa_design(self):
        print(f"{self.name} started to create goa design.")


class Professional(Goaprogrammer, Goadesigner):
    pass

# 2) ახსენით რაში გვჭირდება super()
# super() გამოიყენება მშობელი კლასის მეთოდების ან ატრიბუტების წვდომისთვის, განსაკუთრებით მაშინ, როდესაც გვინდა,
# რომ child კლასმა მშობლის ფუნქციონალიც შეინარჩუნოს და დაამატოს ახალი ფუნქციონალი. 



# 3) ახსენით როგორ მუშაობს super()
# super() ფუნქცია გვაძლევს წვდომას მშობელი კლასის მეთოდებზე და ატრიბუტებზე,
# რაც საშუალებას გვაძლევს გამოვიყენოთ მშობლის კლასის ფუნქციონალი შვილ კლასში.
# super() ფუნქცია ავტომატურად იპოვის მშობელი კლასის პირველი გამოძახების ადგილს,



# 4) გააკეთეთ super()'ის მაგალითი, 
# ანუ აიღეთ რაიმე კლასი და როდესაც მის child class'ს შექმნით დაამატეთ ახალი property  და წამოიღეთ ძველებიც
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super().introduce()
        print(f"My student ID is {self.student_id}.")

student = Student("Alice", 20, "S12345")
student.introduce()