def main():
    pyrramind = int(input("Enter number of blocks "))
    for i in range(pyrramind):
        print_space(pyrramind - i)
        print_block(i)
        print()


def print_space(spc):
    for _ in range(spc + 1):
        print(" ", end="")


def print_block(block):
    for _ in range(block + 1):
        print("#", end="", sep="")


main()
