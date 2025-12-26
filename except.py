# # try:
#     test =int(input("Enter an integer: "))
#
# except ValueError: i am a boyy
#     print("you entered a string")
#
#     print(f"You entered {test}")

# vim is fun
#
# import time

# time.localtime(3.67)
# x = input("Name :")
# print(f"Welcome to vim land,{x}")
# i am usi
def main():
    x = get_int("What is x ")
    print(f"x is {x}")


def get_int(u_input):  #
    while True:
        try:
            collect_input = int(input(f"{u_input}"))
            return collect_input
        except ValueError:
            # print("you entered an non- integer")
            pass


main()
