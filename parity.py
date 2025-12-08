# even_or_odd = int(input("Enter a number "))


# if even_or_odd % 2 == 0:
#     print(f"{even_or_odd} is an even number")

# elif even_or_odd % 2 != 0:
#     print(f"{even_or_odd} is an odd number")
    
# else:
#     print("How did we get here")
    


def is_even(Uinput):
    # return True if Uinput % 2 == 0 else False #pythonic way of doing things 
    return (Uinput%2 == 0) #can be true or false
    

    
even_or_odd = int(input("Enter a number "))


if is_even(even_or_odd):
    print(f"{even_or_odd} is an even number")
else:
    print(f"{even_or_odd} is an odd number")

      