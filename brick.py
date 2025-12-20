# for _ in range(3):
#     print("####")


def main():
#     print_coulmn(10000)
    # print_row(10)
    print_square(6,7)

    
    
def print_square(rows, coulumns):
    for _ in range(rows): # column should be iterrated till completion for each row
        for _ in range(coulumns):
            print("#",end="")# Keep each row on the same line
        print()# move to the next line after each nested iteration

 

# def print_coulmn(coulmn) -> str:
#     for _ in range(coulmn):
#         print("#")

# def print_row(rows): 
#         for _ in range(rows):
#             print("?", end="")

main()