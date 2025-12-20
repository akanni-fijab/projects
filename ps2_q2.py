coke_price = 50
# coin_inserted=0
# amount_due = coke_price -coin_inserted #-> 50
amount_due = 50
print("Amount Due: 50")
while True:
    coin_inserted = int(input("Insert Coin: "))



    if coin_inserted == 5 or coin_inserted==10 or coin_inserted== 25:
        amount_due = amount_due - coin_inserted        
        if amount_due<=0:# check if amount due is negatvie, that is it has been over payed and break
            break
        
    # amount_due = amount_due - coin_inserted # sub initial due amount from inserted coin
    else:
        pass
    print(f"Amount Due: {amount_due}")
    
if amount_due <=0:# negate the negative over payment back to positive
    print(f"Change Owed: {amount_due *-1 }")