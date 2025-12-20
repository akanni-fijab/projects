students = ["Hermione","Harry","Ron"]
for i in range(len(students)):
    # print(student)
    print(i+1,students[i])

    
print(students[0:])

my_dict = {
           "Student":"House",
           "Hermione":"Gryffindor",
           "Harry":"Gryffindor",
           "Ron":"Gryffindor",
           "Draco":"Slytherin",
           }

print(my_dict["Hermione"])

for i in my_dict : # it iterates over the keys
    print(i,my_dict[i],sep=" ,",end="\n\n")# ask interpreter to include values


more_students = [
    {"name": "Hermione", "house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russel Terrier"},
    {"name":"Draco","house":"Slyrherin","patronus":None} #None -> Absence of a value

]

# print(more_students[0])

for element in more_students:
    print(element["name"],element["house"],element["patronus"],sep=", ") # The dicts eith the specified keys