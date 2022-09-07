print('Welcome to the tip calculator.')
total = float(input("What was the total bill? "))

percent_bill = int( input("What percentage tip would you like to give? 10, 12, or 15? "))

quantify = int( input("How many people to split the bill? "))

bill = total * (percent_bill/100)
sumTotal = round( ( (bill + total) / quantify), 2)

#formatação para manter o 0 na segunda casa decimal.
final_amount = "{:.2f}".format(bill)

print(f"Each person should pay: {final_amount}")