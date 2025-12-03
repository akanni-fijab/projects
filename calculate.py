def main():
    user_input = input("Enter some text ")
    print(convert(user_input))
    
def  convert(some_str)->str:
  
    some_str =some_str.replace(":)", "🙂") # It replaces all occurences not just the first
    some_str =some_str.replace(":(", "🙁") 

    return some_str
        

    

main()
