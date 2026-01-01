months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def check_alpha(n):
    try:
        return n.isalpha()
    except TypeError:
        return False


while True:
    u_date = input("Date: ")
    try:
        month, day, year = u_date.split("/")  # remove all '\' characters
        month = int(month)
        day = int(day)
        if month >= 13:  # prompt again for invalid months
            continue
        if day >= 31:
            continue
        day = int(day)
        year = int(year)

        print(f"{year}-{month:02}-{day:02}")  # str formating for double digits
        break
    except ValueError:  # handle when wors are inputed
        if "," in u_date:
            u_date = u_date.replace(",", "")  # remove commas if present

        else:
            continue
        month, day, year = u_date.split(" ")  # remove spaces

        if check_alpha(day):
            continue
        elif not (month.isalpha()) and day.isnumeric() and year.isnumeric():
            continue

        day = int(day)
        if day >= 32:  # skip over invalid days
            continue

        else:
            print(f"{year}-{(months.index(month) + 1):02}-{day:02}")  # str formating
            break
