# 1) ახსენით რა არის კომპოზიცია, რითი განსხვავდება აგრეგაციისგან და გააკეთეთ 1 მაგალითი

# კომპოზიცია არის ობიექტების ურთიერთკავშირი როდესაც ერთი ობიექტი შეიცავს მეორეს
# აგრეგაცია არის ობიექტების ურთიერთკავშირი როდესაც ერთი ობიექტი შეიცავს მეორეს
# მაგრამ ისინი დამოუკიდებლად არსებობენ

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class CarComposition:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine

car1 = CarComposition("Toyota", 99999)
print(f"Car model: {car1.model}, Engine horsepower: {car1.engine.horsepower}")




# 2) განიხილეთ instance, static და class მეთოდები და გააკეთეთ სამივეს მაგალითი

class MyClass:
    class_variable = 0 

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        cls.class_variable += 1
        return cls.class_variable

    @staticmethod
    def static_method():
        return "This is a static method."
    
# 3) გაიხსენეთ და ახსენით რა არის multiple და multilevel inheritance

# Multiple inheritance არის როდესაც კლასი მემკვიდრეობს რამდენიმე კლასიდან.
# Multilevel inheritance არის როდესაც კლასი მემკვიდრეობს კლასიდან, რომელიც უკვე მემკვიდრეობს სხვა კლასიდან.

# 4) მოიყვანეთ მაგალითი რა შემთხვევაში დაგვჭირდება data hiding და გააკეთეთ მსგავსი რამ კოდით
