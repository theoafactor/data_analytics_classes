import csv

answer = open("answer2.csv", "w")

csv_writer = csv.writer(answer)

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

csv_writer.writerow(["name", "email", "age_in_years", "gender"])

for student in students:
    csv_writer.writerow(student.values())

answer.close()