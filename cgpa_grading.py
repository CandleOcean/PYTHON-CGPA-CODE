print("\n")
name = input("Enter your full name: ")
course = input("Enter your course units here(You can separate them using ',' ): \n")
course_units = course.split(",")

obj = dict()
for unit in course_units:
    obj[unit] = int(input("Enter the credit units for the corresponding course units: "))
print("\n")
print(obj)
total_credit_units = sum(obj.values())

print("\n")
mks = input("Enter the target marks for the corresponding course units(marks should be in the range of 0-100): \n "
            "separate them using a ',': \n")

marks = mks.split(",")

obj3 = dict()
count = 0
for mark in marks:
    if 80 <= int(mark) <= 100:
        grade = 'A'
        grade_point = 5.0
        print(f" For {course_units[count]}, grade is 'A'")
    elif int(mark) >= 75:
        grade = 'B+'
        grade_point = 4.5
        print(f" For {course_units[count]}, grade is 'B+'")
    elif int(mark) >= 70:
        grade = 'B'
        grade_point = 4.0
        print(f" For {course_units[count]}, grade is 'B'")
    elif int(mark) >= 65:
        grade = 'C+'
        grade_point = 3.5
        print(f" For {course_units[count]}, grade is 'C+'")
    elif int(mark) >= 60:
        grade = 'C'
        grade_point = 3.0
        print(f" For {course_units[count]}, grade is 'C'")
    elif int(mark) >= 55:
        grade = 'D+'
        grade_point = 2.5
        print(f" For {course_units[count]}, grade is 'D+'")
    elif int(mark) >= 50:
        grade = 'D'
        grade_point = 2.0
        print(f" For {course_units[count]}, grade is 'D'")
    else:
        grade = 'F'
        grade_point = 0.0
        print(f" For {course_units[count]}, grade is 'F'")

    count = count + 1

    obj3[mark] = grade_point

track = 0
gp_cu = 0
while track < len(course_units):
    gp_cu = gp_cu + (obj3[marks[track]] * obj[course_units[track]])
    track = track + 1

print("\n")
print(f"{name}, Your total of grade points and credit units is {gp_cu}")

GPA = gp_cu / total_credit_units
gpa_to_two_decimal = "{:.2f}".format(GPA)


print(f"{name}, Your GPA is {gpa_to_two_decimal}")

if 4.4 <= GPA <= 5.0:
    print(f"{name}, you have a first class degree")
elif GPA >= 3.6:
    print(f"{name}, you have a second class degree upper")
elif GPA >= 2.8:
    print(f"{name}, you have a second class degree lower")
else:
    print(f"{name}, you have failed")

print("\n")
print("I advise you to raise your target mark by at least 5% !")
advice = input("if you take my advice, write Y or N if you don't: ")
print("\n")

count1 = 0
if advice == 'Y' or advice == 'y':
    increase_target_mark = float(5.0/100) * float(mark)

    for mark in marks:
        if 80 <= int(mark) + increase_target_mark <= 100:
            grade = 'A'
            grade_point = 5.0
            print(f" For {course_units[count1]}, grade grade would be 'A'")
        elif int(mark) + increase_target_mark >= 75:
            grade = 'B+'
            grade_point = 4.5
            print(f" For {course_units[count1]}, grade grade would be 'B+'")
        elif int(mark) + increase_target_mark >= 70:
            grade = 'B'
            grade_point = 4.0
            print(f" For {course_units[count1]}, grade grade would be 'B'")
        elif int(mark) + increase_target_mark >= 65:
            grade = 'C+'
            grade_point = 3.5
            print(f" For {course_units[count1]}, grade grade would be 'C+'")
        elif int(mark) + increase_target_mark >= 60:
            grade = 'C'
            grade_point = 3.0
            print(f" For {course_units[count1]}, grade grade would be 'C'")
        elif int(mark) + increase_target_mark >= 55:
            grade = 'D+'
            grade_point = 2.5
            print(f" For {course_units[count1]}, grade grade would be 'D+'")
        elif int(mark) + increase_target_mark >= 50:
            grade = 'D'
            grade_point = 2.0
            print(f" For {course_units[count1]}, grade grade would be 'D'")
        else:
            grade = 'F'
            grade_point = 0.0
            print(f" For {course_units[count1]}, grade would be  'F'")

        count1 = count1 + 1

        obj3[mark] = grade_point

    track = 0
    gp_cu = 0
    while track < len(course_units):
        gp_cu = gp_cu + (obj3[marks[track]] * obj[course_units[track]])
        track = track + 1

    print("\n")
    print(f"{name}, Your total of grade points and credit units grade would be  {gp_cu}")

    GPA = gp_cu / total_credit_units
    gpa_to_two_decimal = "{:.2f}".format(GPA)
    print(f"{name}, Your GPA would be {gpa_to_two_decimal}")

    if 4.4 <= GPA <= 5.0:
        print(f"{name}, you would have a first class degree")
    elif GPA >= 3.6:
        print(f"{name}, you would have a second class degree upper")
    elif GPA >= 2.8:
        print(f"{name}, you would have a second class degree lower")
    else:
        print(f"{name}, you would have failed")

elif advice == 'N' or advice == 'n':
    quit(f"GOOD BYE {name}")
else:
    quit("Wrong input")

