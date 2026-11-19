class Student:
    print("Python read the Student blueprint")
    school = "Surprise school"
    grade = 10
    print("Class variable grade:", grade)

anna = Student()
ryan = Student()
print("anna is a", type(anna))  


print("anna's school:", anna.school, "| ryan's garde:", ryan.grade)
new_grade = int(input("New class Grade?"))
Student.grade = new_grade
print("After changing the class grade: anna", anna.grade,"| ryan", ryan.grade)

anna.grade = 12
print("anna", anna.grade,"| ryan", ryan.grade, "| Student", Student.grade)