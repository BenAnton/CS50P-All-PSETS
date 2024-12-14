def coke():
    amount_due = 50
    current_balance = 0



    while amount_due > 0:

        coin = input(f"Amount Due: {amount_due}\n")
        coin = int(coin)

        if coin == 5 or coin == 10 or coin == 25:
            amount_due -= coin
            current_balance += coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")

        if amount_due <= 0:
            return print(f"Change Owed: {current_balance - 50}")

coke()
