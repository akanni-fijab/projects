# match keyword of a thing
#harry potter stuff

name = input("Name please 🧙 ")
# name.lower() # return a new string with the required formatting
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Wait a minute, who are you")


match name.lower():
    case "harry" | "hermione" | "ron": # --> or keyword equivalent
        print("Gryffindor")
    case "draco":
        print("Slythrin")
    case _:
        print("Wait a minute, who are you???") #--> basically else or a catch all  
    