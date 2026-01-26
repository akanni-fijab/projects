list_of_names = []
# Refactor in to a function
while True:
    try:
        name = input("Name: ")
        list_of_names.append(name)
    except EOFError:
        if len(list_of_names) == 0:
            break

        elif len(list_of_names) == 1:
            print()  # all i dad to do was add this to push it into a new line no need to Refactor
            print(f"Adieu, adieu, to {list_of_names[0]}")
            break
        elif len(list_of_names) == 2:
            print()
            print(f"Adieu, adieu, to {list_of_names[0]} and {list_of_names[1]}")
            break
        else:
            print()
            print("Adieu, adieu, to ", end="")
            for i in range(len(list_of_names) - 1):
                print(list_of_names[i], end=", ")
            print(f"and {list_of_names[-1]}")
            break
