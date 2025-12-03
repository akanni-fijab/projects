print("DO I STILL REMEMBER PYTHON")
import func_imports


x = int(input("Enter x val ")) # Inner most function is evaluated first
y = int(input("Enter Y val ")) #Square brackets in documentation mean optional parameters


# print(x / y)
print(f"The square of {x} is {func_imports.square_input(x)}")
print(f"The square of {y} is {func_imports.square_input(y)}")

print(f"{x} raised to power {y} is {func_imports.pow(x,y)}")
print(f"{y} raised to power {x} is {func_imports.pow(y,x)}")


# print(f"{x/y:,.32f}")
  
