class Animal:
    def speak(self):
        print("Animal sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d=Dog()
d.speak()
d.bark()