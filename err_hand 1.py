# problem set 1
#
#
#
def main():
    while True:
        try:
            fraction = input("fraction: ")
            x, y = fraction.split("/")  # obtain x and y

            x = int(x)  # typecast them to ints
            y = int(y)
            if x > y:
                pass
            elif x < 0:
                pass
            elif x is float:  # force the user to enter an int
                pass
            else:
                fuel = print_percent(x, y)  # store the return value
                print(fuel)
                break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def print_percent(x, y):
    division = x / y
    mult = division * 100
    mult = round(mult)

    if x > y:
        pass
    elif division * 100 == 25:
        return "25%"
    elif division * 100 == 50:
        return "50%"
    elif division * 100 == 75:
        return "75%"
    elif (division * 100) >= 99 and (division * 100) <= 100:
        return "F"
    elif (division * 100) <= 1:
        return "E"
    else:  # prints out a percentage for every other percentage
        return f"{mult}%"


main()
