
def calculate(grades):
    total = sum(grades)
    count = len(grades)
    average = total / count
    return average

n = int(input("enter the number of courses: "))
grades = []

for i in range(n):
    grade = float(input(f"enter grade {i+1}: "))
    grades.append(grade)


average = calculate(grades)

print(f"Average: {average:.2f}")


if average >= 17:
    print("great!")
elif average >= 10:
    print("pass")
else:
    print("fail")









































