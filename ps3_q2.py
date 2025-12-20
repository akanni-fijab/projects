vowels = ("a","e","i","o","u")
vowels_removed=[]



text = input("Input: ")

for i in text:
    if i.lower() in vowels:
        text=text.replace(i,"")

# print(f"Output : {vowels_removed}")
# for i in vowels_removed:
#     print(i,end="")


print(text)
