
def calculate_student_gpa(student_dict):
    grades = student_dict["grades"]
    return sum(grades) / len(grades)

students_list = [
    {
        "student_id": 1,
        "name": "aylin",
        "grades": [18, 19.5, 10]
    },
    {
        "student_id": 2,
        "name": "armin",
        "grades": [15, 20, 16.5]
    }
]

for student in students_list:
    gpa = calculate_student_gpa(student)
    print(f"{student['name']} gpa :{gpa}")