# given variables
balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04

# set variables
month = 1
totalPaid = 0
monthlyInterestRate = annualInterestRate / 12

while month < 13:
    # set minPayment, balance
    minPayment = balance * monthlyPaymentRate

    # month
    print("Month: " + str(month))
    month += 1

    # payment
    print("Minimum monthly payment: " + str(round(minPayment, 2)))
    totalPaid += minPayment

    newBalance = (balance - minPayment)*(1 + monthlyInterestRate)
    print("Remaining balance: " + str(round(newBalance, 2)))

    balance = newBalance

print('Total paid: ' + str(round(totalPaid, 2)))
print('Remaining balance: ' + str(round(balance, 2)))
