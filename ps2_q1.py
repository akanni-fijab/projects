# my_list =[1,2,34,6,74,2,1,4,42,1,42,67,324,5,6,5,4532313,432,4,2,425,36,63,256,35,36,1,56,653,120]

# odd = [i%2==0 for i in my_list]

# print(odd)


str_input = input("camelCase: ")
# str_input.
snake_case=[]# only modifiable and appendable data type with out key value pairs
for i in str_input:
    if i.isupper(): # check if each char is capital
        i = i.lower() # convert to lower_case
        snake_case.append("_")# append underscore for snakeCase
        snake_case.append(i) #append lower case char
    else:
        snake_case.append(i) # appned if already lower

print("snake_case: ",end="")
    
for i in snake_case:
    print(i,end="")# print out all the elements of the list 
print()

    

