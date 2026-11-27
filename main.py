def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)

    print("Student Final Total Marks:", total)
    print("Percentage:", percentage)

    if percentage >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


# Student marks in five subjects
marks = [80, 75, 90, 85, 70]

calculate_result(marks)