def main():

    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word) -> str:
    vowels = ("a", "e", "i", "o", "u")
    for i in word:
        if i.lower() in vowels:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
