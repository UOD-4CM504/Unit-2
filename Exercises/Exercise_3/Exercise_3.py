# Please do not edit this, otherwise you will not pass the tests
no_child = int(input("How many child tickets would you like?\n"))
no_adult = int(input("How many adult tickets would you like?\n"))
no_senior = int(input("How many senior tickets would you like?\n"))

total = no_child*5 + no_adult*10 + no_senior*8

print(f"Total Price: £{total}")