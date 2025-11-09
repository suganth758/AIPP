class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Major: {self.major}")

# Example usage:
student1 = Student("Alice", 20, "Computer Science")
student1.display_info()