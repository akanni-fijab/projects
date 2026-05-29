students = []

with open("students.csv") as file:
    for line in file:
        name, house, home = line.rstrip().split(",")

        student = {
            "name": name,
            "house": house,
            "home": home,
        }  # each entry in the list is a dict of name anf house
        students.append(student)


def get_name(student):
    return student["name"]


for student in sorted(students, key=lambda student: student["name"]):
    print(
        f" {student['name']} is in {student['house']} and grew up in {student['home']}"
    )

# Code below for file creation and appending
# name = input("Name, Abeg? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")  # no need to close files mehn
#
#
#
# names = []
# with open("names.txt", "r") as file:
#     for line in file:
#         names.append(line)
#         # print(f"hello, {line.rstrip()} ")
# #     lines = file.readlines()
# #
# for name in sorted(names):
#     print(name.rstrip())
# for line in lines:
#     print(line.rstrip())
#

# for _ in range(4):
#     name = input("Name, Abeg? ")

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
#
