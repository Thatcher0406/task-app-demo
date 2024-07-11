# Define the Student class
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

# Define the Classroom class
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students in the class.")
        else:
            print("List of Students:")
            for idx, student in enumerate(self.students, start=1):
                print(f"Student {idx}: {student.name}")

    def get_student_average_grade(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                avg_grade = student.get_average_grade()
                print(f"Average grade for {student.name}: {avg_grade:.2f}")
                return
        print(f"Student '{student_name}' not found.")

    def get_class_average_subject(self, subject):
        total_grades = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total_grades += student.grades[subject]
                count += 1
        if count > 0:
            class_avg = total_grades / count
            print(f"Class average for {subject}: {class_avg:.2f}")
        else:
            print(f"No grades found for subject '{subject}'.")

# Demo of functionalities
if __name__ == "__main__":
    classroom = Classroom()

    # Adding students
    student1 = Student("Alice")
    student1.add_grade("Math", 85)
    student1.add_grade("Science", 90)
    classroom.add_student(student1)

    student2 = Student("Bob")
    student2.add_grade("Math", 75)
    student2.add_grade("Science", 80)
    classroom.add_student(student2)

    # Display all students
    classroom.display_students()

    # Get average grade for a student
    classroom.get_student_average_grade("Alice")

    # Get class average for a subject
    classroom.get_class_average_subject("Science")
