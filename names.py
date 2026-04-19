# Code below for file creation and appending
# name = input("Name, Abeg? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")  # no need to close files mehn
#
#
#
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line)
        # print(f"hello, {line.rstrip()} ")
#     lines = file.readlines()
#
for name in sorted(names):
    print(name.rstrip())
# for line in lines:
#     print(line.rstrip())
