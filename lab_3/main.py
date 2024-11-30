from student_model import student
from course_model import course
from student_course import student_course

#test student model
student(1, "mahmoud", 19, "mahmoudfawzy@gmail.com")
student(2, "Ebrahim", 19, "Ebrahim@gmail.com")
 
#test course model
course(1, "python", 100)
course(2, "java", 99)

#test course model
student_course(1, 1, 90)
student_course(2, 2, 84)

#If you want to test the code just remove the existing lines in the CSV files