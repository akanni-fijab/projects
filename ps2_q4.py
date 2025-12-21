
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

"""


    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

"""
def is_valid(s):
    def start_with_alpha(s):
        first_two = s[0:2]
        return  first_two.isalpha() # --> returns true or false

    def plate_no_size(s): # Make sure within size limit
        if 2<= len(s) <= 6:
            return True
        else:
            return False
   

    def read_plate(s)-> bool:
        is_digit = False
        for i in s:
            if i.isnumeric():
                if is_digit == False:
                    if i =="0":
                        return False
                
                is_digit=True
                    

              
            elif is_digit == True:
                return False
        return True  
    

    def check_punctuation(s):
        punctuation = (".","?","!",",",";",":","-","(",")","[","]","{","}","'","\"",)
        for i in s:
            if i in punctuation:
                return False
            
        return True

    return plate_no_size(s) and start_with_alpha(s)  and read_plate(s) and check_punctuation(s)





main()

