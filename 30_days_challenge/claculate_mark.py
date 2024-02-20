# qus : get the student name and subject marks after find total mark and % of mark

student_name = input("Enter name: ")
number_of_subject = int(input("Enter number of subjects: "))
marks = 0
for i in range(number_of_subject):
    mark = int(input("Enter subject mark: "))
    if mark <= 100:
        marks = mark + marks
    else:
        print("please enter your correct mark ")
print("Student_name: ", student_name)
print("Over all mark: ", marks)
print("Percentage of mark: ", (marks / (number_of_subject*100))*100)
