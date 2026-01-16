import pyfiglet
import sys
import random

figlet = pyfiglet.Figlet()

my_obj = figlet.getFonts()
my_obj = list(my_obj)

# j_obj = json.dumps(my_obj, indent=2)
# print(j_obj)

fig_font = ""
font_choose = ["-f", "--font"]
if len(sys.argv) == 1:  # no input
    u_string = input("Input: ")  # Pick random font with input

    figlet.setFont(font=random.choice(my_obj))
    print(f"{figlet.renderText(u_string)}")

elif sys.argv[1] in font_choose:  # entered a flag so some input required
    fig_font = sys.argv[2]
    figlet.setFont(font=sys.argv[2])

    u_string = input("Input: ")
    print(figlet.renderText(u_string))

elif (
    sys.argv[1] not in my_obj or sys.argv[1] is None
):  # char us in argv[1] but might be Invalid
    sys.exit("Invalid figlet font")

# else:
#     u_string = input("Input: ")
#
#     figlet.setFont(font=random.choice(my_obj))
#     print(f"{figlet.renderText(u_string)}")
