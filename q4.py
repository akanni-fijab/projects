get_ints = input("Expression ")

x,z,y = get_ints.split(" ")# Don' over complicate shit
print(x)
print(type(z))
print(y)
x = float(x)
y = float(y)



match z:
    case "+":
        print(x + y)
    case "-":
        print(x -y)
    case "*":
        print(x * y)
    case "/":
        print(x/y)
