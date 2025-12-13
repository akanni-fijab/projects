get_extension = input("File name: ").lower().strip()
*file_name, extension = get_extension.split(".") #change what is not being compares to a list
# print(file_name)
# print(extension)

# #I'm guessing the * just creates a list
# print(type(extension))

match extension:
    case "gif":
        print("image/gif")
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")


        
