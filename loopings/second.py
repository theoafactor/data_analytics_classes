students = [
    {
        "name": "James John",
        "age": 12,
        "class": "class 1",
        "email": "james@gmail.com"
    },
    {
        "name": "Jerry Matt",
        "age": 13,
        "class": "class 2",
        "email": "jerry@gmail.com"
    }, 
    {
        "name": "Mary Joseph",
        "age": 11,
        "class": "class 2",
        "email": "mary@gmail.com"
    }
]

counter = 0
while counter < len(students):
    print("Good afternoon ", students[counter]['name'], " your email is ", students[counter]['email'] )
    counter = counter + 1