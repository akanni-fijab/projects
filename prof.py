import random


def main():
    game_level = get_level()
    user_score = 0
    for i in range(10):
        x = generate_integer(game_level)
        y = generate_integer(game_level)
        for j in range(3):
                try:
                    ans = input(f"{x} + {y} = ")
                    if int(ans) == int(x + y):
                        user_score += 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
                if j == 2:
                    print(f"{x} + {y} = {x + y}")
    print(user_score)


def get_level():
    levels = [1, 2, 3]
    while True:  # obtain level from user input
        try:
            u_level = int(input("Level: "))
            if u_level in levels:
                return u_level
        except ValueError:
            continue


def generate_integer(level):
    ##############
    # generate random keys of size 1,2,3

    if level == 1:
        random_no = random.randint(0, 9)
    elif level == 2:
        random_no = random.randint(10, 99)
    elif level == 3:
        random_no = random.randint(100, 999)
    else:
        raise ValueError

    return random_no


if __name__ == "__main__":
    main()
