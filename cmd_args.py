import cowsay
import sys

my_fish = r"""
\
 \  
        /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
"""

# cowsay.draw("I am using a venv baby", my_fish)
#
#
try:
    if sys.argv[1] == "tux":
        print(cowsay.get_output_string("tux", "I use arch Btw"))
    elif sys.argv[1] == "milk":
        print(cowsay.get_output_string("milk", "I use arch Btw"))
except IndexError:
    cowsay.draw("Enter something na", my_fish)
    sys.exit("Invalid cowsayer")


# print(sys.argv[0])


# if len(sys.argv) < 3:
#     sys.exit("too Few args")
# elif len(sys.argv) > 3:
#     sys.exit("too many args")

# print(sys.argv[1], sys.argv[1])

# try:
#     print(f"you entered the flag {sys.argv[1]}")
# except IndexError:
#     print("not enough cmd elements")
#
# print()
#
#
# for arg in sys.argv[1:]:
#     print(arg)
#
