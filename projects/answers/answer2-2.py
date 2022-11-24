import csv

students = [
    {
        "name": "James John",
        "email": "james@gmail.com",
        "age_in_years": 12,
        "gender": "male"
    },

    {
        "name": "Jerry Adams",
        "email": "jerry@gmail.com",
        "age_in_years": 11,
        "gender": "males"
    },

    {
        "name": "Andrew Jacob",
        "email": "andrew12@gmail.com",
        "age_in_years": 13,
        "gender": "male"
    },

    {
        "name": "Akeem Adeyemi",
        "email": "ak2000@gmail.com",
        "age_in_years": 14,
        "gender": "male"
    },

    {
        "name": "Mary Joseph",
        "email": "maryjos@gmail.com",
        "age_in_years": 13,
        "gender": "female"
    },

    {
        "name": "Lola Abraham",
        "email": "lolaabraham@gmail.com",
        "age_in_years": 12,
        "gender": "male"  

    }

]

adjusted_students = []
for student in students:
    new_student = {}
    names = student["name"].split(" ")
    firstname = names[0]
    lastname = names[1]
    student.pop("name")
    new_student["firstname"] = firstname
    new_student['lastname'] = lastname
    new_student['email'] = student['email']
    new_student['age_in_years'] = student['age_in_years']
    new_student['gender'] = student['gender']
    adjusted_students.append(new_student)





## print(students)

answer = open("answer2-2.csv", "w")

csv_writer = csv.writer(answer)

csv_writer.writerow(["firstname","lastname", "email", "age_in_years", "gender"])

for student in adjusted_students:
    csv_writer.writerow(student.values())


answer.close()






