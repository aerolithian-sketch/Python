def calculate_change(paid, price):
    change = paid - price
    return change

snack1_price = 25
snack2_price = 30
drink1_price = 20

print("=== Snack Vending Machine ===")
while True:
    print("We have the following items available:")
    print("1. Snack 1 - 25 units")
    print("2. Snack 2 - 30 units")
    print("3. Drink 1 - 20 units")
    choice = int(input("Please select an item (1-3): "))
    if choice == 1:
        snack_price = snack1_price
        break
    elif choice == 2:
        snack_price = snack2_price
        break
    elif choice == 3:
        snack_price = drink1_price
        break
    else:
        print("Invalid choice. Please select a valid item.")

print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25 units\n")


total_inserted = 0
coins_inserted = 0
money_remaining = snack_price - total_inserted

while True:
    coin = int(input("Insert a coin (1, 5, 10, 25): "))
    if coin != 1 and coin !=5 and coin != 10 and coin != 25:
        print("Invalid coin. Please insert a valid coin.")
        continue
    total_inserted += coin
    coins_inserted += 1
    money_remaining = snack_price - total_inserted
    print(f"Inserted: {coin}. Total so far: {total_inserted} units.")
    print(f"Money remaining: {money_remaining} units.\n")
    if total_inserted >= snack_price:
        print("Enough money inserted!\n")
        break
change_due = calculate_change(total_inserted, snack_price)
print("Dispensing snack...")
if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units.")

print("\n=== PURCHASE SUMMARY ===")
print("Snack Price: ", snack_price)
print("Coins Inserted: ", coins_inserted)
print("Total Paid: ", total_inserted)
print("Change Given: ", change_due)
print("Thank you for your purchase!")
print("=== END OF TRANSACTION ===")
