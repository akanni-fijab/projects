# while True:
#     n = int(input("What is n? "))
#     if n < 0:
#         print("Enter a positive interger")
#         continue

#     elif n>0:
#         for _ in range(n):
#             print("meow ")
#         break    






# Meow function 

def main():
    n = get_number()
    meow(n)

def get_number()-> int :
    n_meows =int(input("What is n? "))
    # return n_meows
    while True:
        if n_meows > 0:
            return n_meows
        


def meow(n) -> str:
    for _ in range(n):
        print("meow")



    ...
    
    

main()