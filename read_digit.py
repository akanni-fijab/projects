"""
seen_digit ← false

FOR each character c in plate FROM left to right
    IF c is a digit THEN
        IF seen_digit is false THEN
            IF c == '0' THEN
                RETURN false   // first number cannot be 0
            END IF
            seen_digit ← true  // numbers start here
        END IF
    ELSE   // c is a letter
        IF seen_digit is true THEN
            RETURN false       // letter after number is invalid
        END IF
    END IF
END FOR

RETURN true

"""

def read_plate(s)-> bool:
    is_digit = False
    for i in s:
        if i.isnumeric():
            is_digit=True
        elif is_digit == True:
            return False
    return True
            
        

# l =""
# l.is

l="12345op"

for i in l:
    print(i.isnumeric())