import csv

name: str = input("What is your name? :")
home: str = input("What is your home? :")


with open("student.csv", "a") as file:
    wirter_obj = csv.DictWriter(
        file, fieldnames=["name", "home"]
    )  # writer name causes name clash
    wirter_obj.writerow({"name": name, "home": home})
