class Student:
    """Represents a student with their personal details and academic marks."""

    def __init__(self, full_name, age):
        """
        Initializes a new Student instance.

        Args:
            full_name (str): The full name of the student.
            age (int): The age of the student.
        """
        self.full_name = full_name  # Renamed 'name' to 'full_name' for clarity
        self.age = age
        self.marks = []  # Stores marks in a list as requested

    def add_mark(self, mark):
        """
        Adds a single mark to the student's list of marks.

        Args:
            mark (float or int): The mark to add.
        """
        if isinstance(mark, (int, float)) and 0 <= mark <= 100:
            self.marks.append(mark)
        else:
            print(f"Invalid mark: {mark}. Marks should be a number between 0 and 100.")

    def get_average_mark(self):
        """
        Calculates and returns the average of the student's marks.

        Returns:
            float: The average mark, or 0.0 if no marks have been added.
        """
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def get_student_info(self):
        """
        Returns a string containing the student's information.

        Returns:
            str: A formatted string with student name, age, and marks.
        """
        return (
            f"Student Name: {self.full_name}\n"
            f"Age: {self.age}\n"
            f"Marks: {self.marks if self.marks else 'No marks added yet'}\n"
            f"Average Mark: {self.get_average_mark():.2f}"
        )

# Example Usage:
print("--- Student 1 ---")
student1 = Student("Alice Smith", 18)
student1.add_mark(85)
student1.add_mark(92.5)
student1.add_mark(78)
print(student1.get_student_info())

print("\n--- Student 2 ---")
student2 = Student("Bob Johnson", 19)
student2.add_mark(70)
student2.add_mark(65)
student2.add_mark("invalid") # Test invalid mark
print(student2.get_student_info())