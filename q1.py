u_input = input("What is the answer to the Great Question of Life, the Universe and Everything, outputting ")
# if u_input == "42" or u_input.lower() =="forty-two" or u_input.lower() == "forty two":
#     print("Yes")
# else:
#     print("No")
# Why was i converting to int???

match u_input.lower():
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _ :
        print("No")