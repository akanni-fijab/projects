def main():
    list_of_names = []
    while True:
        try:
            name = input("Name: ")
            list_of_names.append(name)
            # adeiu_return(list_of_names)
        except EOFError:
            print()
            print(adeiu_return(list_of_names))
            break


def adeiu_return(a_list):
    a_list = list(a_list)
    if len(a_list) == 0:
        return None

    elif len(a_list) == 1:
        return f"Adieu, adieu, to {a_list[0]}"

    elif len(a_list) == 2:
        return f"Adieu, adieu, to {a_list[0]} and {a_list[1]}"
    else:
        first_strings = str(a_list[:-1])
        first_strings = first_strings.replace("[", "")  # do this for and
        first_strings = first_strings.replace("]", "")
        first_strings = first_strings.replace("'", "")

        last_strings = str(a_list[-1])  # returned with and

        # print(f"Adieu, adieu, to {first_strings}, and {last_strings}")
        return f"Adieu, adieu, to {first_strings}, and {last_strings}"


main()
#
# la = [1, 2, 3, 4]

# adeiu_return(la)
# print(adeiu_return(la))
