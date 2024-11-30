import csv

def student_course(student_id, course_id, grade=None):
    student_course_info = {}
    if not isinstance(student_id, int) or not isinstance(course_id, int):
        raise ValueError("Both student_id and course_id must be integers")
    else:
        with open("student_course.csv", "r") as file:
            for line in file:
                parts = line.split(",")
                if parts[0] == (str(student_id)) and parts[1] == (str(course_id)):
                    raise Exception("this student is already exist in this course")
            
    student_course_info["student_id"] = student_id
    student_course_info["course_id"] = course_id
    if grade is not None:
        student_course_info["grade"] = grade

    with open("student_course.csv", "a") as file:
        field_names = ["student_id", "course_id", "grade"]
        writer = csv.DictWriter(file, fieldnames=field_names)

        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(student_course_info)

        return student_course

    
