greeting = input("Greeting: ").lower().strip()



# print(get_money)
# print(rest)


    

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")