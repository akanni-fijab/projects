def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    def start_with_alpha(s):
        first_two = s[0:2]
        return first_two.isalpha()  # --> returns true or false

    def plate_no_size(s):  # Make sure within size limit
        if 2 <= len(s) <= 6:
            return True
        else:
            return False

    def read_plate(s) -> bool:
        is_digit = False
        for i in s:
            if i.isnumeric():
                if is_digit is False:
                    if i == "0":
                        return False

                is_digit = True

            elif is_digit is True:
                return False
        return True

    def check_punctuation(s):
        punctuation = (
            ".",
            "?",
            "!",
            ",",
            ";",
            ":",
            "-",
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
            "'",
            '"',
        )
        for i in s:
            if i in punctuation:
                return False

        return True

    return (
        plate_no_size(s)
        and start_with_alpha(s)
        and read_plate(s)
        and check_punctuation(s)
    )


if __name__ == "__main__":
    main()
