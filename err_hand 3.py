grocerys = {}

while True:
    try:
        store_item = input()
        # if item  in dict then dict[item]+=1 set the default to zero

        if store_item == "\n":  # don't add enter keys ie \n chatacters
            pass
        elif store_item in grocerys:
            grocerys[store_item] += 1  # increment when item in dict
        # else update it to key:0
        else:
            grocerys.update([(store_item, 1)])  # start count at 1 for jew dict entries

    except EOFError:
        sorted_grocey = sorted(grocerys)  # creates a sorted list
        for i in sorted_grocey:
            print(grocerys[i], i.upper())
        break
