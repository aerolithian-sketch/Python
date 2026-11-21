def total_calc(bill_amount, tip_perc):
    total=bill_amount * (1 + tip_perc / 100)
    total=round(total, 2)
    print(f"Total amount to be paid is: ${total}")
total_calc(150, 20)