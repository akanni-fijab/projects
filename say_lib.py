def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye {name}")


# def main():
#     hello("world")
#     goodbye("world")

if (
    __name__ == "__main__"
):  # Runs the code if the file itself is ran ran or the main func is used i guess:world
    main()
