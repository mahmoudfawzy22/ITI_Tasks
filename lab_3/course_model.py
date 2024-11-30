import csv 

def course(course_id, name, max_grade):

    course_info = {}

    if not isinstance(course_id, int):
        raise ValueError("course_id must be integer")
    else:
        with open("course.csv") as file:
            check = True
            for line in file:
                if line.startswith(str(course_id)):
                    check = False
                    break
            if check:
                course_info["course_id"] = course_id
            else:
                raise Exception("course_id must be unique")
    
    if not isinstance(name, str):
        raise NameError("name must be string")
    else:
        course_info["name"] = name
    
    if not isinstance(max_grade, int):
        raise ValueError("max grade must be integer")
    else:
        course_info["grade"] = max_grade
    
    with open("course.csv", "a") as file:
        field_names = ["course_id", "name", "grade"]
        writer = csv.DictWriter(file, fieldnames=field_names)

        if file.tell() == 0:
             writer.writeheader()
        writer.writerow(course_info)

    return course_info["course_id"]