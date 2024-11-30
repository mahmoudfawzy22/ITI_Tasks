import re
import csv

def student(id, name, age, email):
    student_info = {}
    if not isinstance(id, int):
        raise ValueError("id must be an integer")
    else:
        with open("student.csv", "r") as file:
            check = True
            for line in file:
                if line.startswith(str(id)):
                    check = False
                    break
            if check == True:
                student_info["student_id"] = id
            else:
                raise Exception("id is not valid, id must be unique")
    
    if not isinstance(name, str):
        raise NameError("name must be a string")
    student_info["name"] = name

    if not isinstance(age, int):
        raise ValueError("age must be an integer")
    student_info["age"] = age

    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError("email is not valid")
    else:
        student_info["email"] = email

    with open("student.csv", "a") as file:
        field_names = ["student_id", "name", "age", "email"]  
        writer = csv.DictWriter(file, fieldnames=field_names)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(student_info)

    return student_info["student_id"]
