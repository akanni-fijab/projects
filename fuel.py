def main(): ...


def convert(fraction) -> float:
    x, y = fraction.split("/")
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        raise ValueError
    if x < 0:
        raise ValueError

    if y < 0:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    fraction = x / y

    return fraction * 100


def gauge(percentage) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
