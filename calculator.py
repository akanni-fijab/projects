def main():
    x = input("What is x ? ")
    print(f"the square of {x} is {square(x)}")


# Better to use functions
# for easy testing 11:10:03
# 2026-03-29 11:10


def square(n):
    return n * n


if __name__ == "__main__":  # only run main() when file is run itself
    main()
