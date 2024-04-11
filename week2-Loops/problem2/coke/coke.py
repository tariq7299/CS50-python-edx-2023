

# First Solution
# amount_due = 50

# while amount_due > 0:
#     print("Amount Due:", amount_due)
#     inserted_coins = int(input("Insert Coin: "))
#     if inserted_coins in [5, 10, 25, 50]:
#         amount_due -= inserted_coins


# change_owed = abs(amount_due)
# print("Change Owed:", change_owed)



# Second solution

amount_due = 50
change_owed = 50
inserted_coins_sum = 0

print("Amount Due", amount_due)
inserted_coins = int(input("Insert Coin: "))

while amount_due > 0:

    if inserted_coins == 50:
        amount_due = amount_due - 50
        change_owed = change_owed - 50
        inserted_coins_sum += inserted_coins
        if change_owed <= 0 or inserted_coins_sum >= 50:
            print("Change Owed: ", abs(change_owed))
            break
        print("Amount Due:", amount_due)
        inserted_coins = int(input("Insert Coin: "))

    elif inserted_coins == 25:
        amount_due = amount_due - 25
        change_owed = change_owed - 25
        inserted_coins_sum += inserted_coins
        if change_owed <= 0 or inserted_coins_sum >= 50:
            print("Change Owed:", abs(change_owed))
            break
        print("Amount Due:", amount_due)
        inserted_coins = int(input("Insert Coin: "))

    elif inserted_coins == 10:
        amount_due = amount_due - 10
        change_owed = change_owed - 10
        inserted_coins_sum += inserted_coins
        if change_owed <= 0 or inserted_coins_sum >= 50:
            print("Change Owed:", abs(change_owed))
            break
        print("Amount Due:", amount_due)
        inserted_coins = int(input("Insert Coin: "))

    elif inserted_coins == 5:
        amount_due = amount_due - 5
        change_owed = change_owed - 5
        inserted_coins_sum += inserted_coins
        if change_owed <= 0 or inserted_coins_sum >= 50:
            print("Change Owed:", abs(change_owed))
            break
        print("Amount Due:", amount_due)
        inserted_coins = int(input("Insert Coin: ")
                             )
    else:
        print("Amount Due:", amount_due)
        inserted_coins = int(input("Insert Coin: "))


