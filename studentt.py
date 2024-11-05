students_grades = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 88},
    {"name": "Eva", "grade": 91}
]
def calculate_average(grades):
    total = sum(grades)
    count = len(grades)
    return total / count if count > 0 else 0
grades = [student["grade"] for student in students_grades]
average_grade = calculate_average(grades)
with open("average_grade.txt", "w") as file:
    file.write(f"Average grade of students: {average_grade:.2f}\n")
    file.write("\nStudent Grades:\n")
    for student in students_grades:
        file.write(f"{student['name']}: {student['grade']}\n")
print("Average grade and student data have been written to 'average_grade.txt'.")
