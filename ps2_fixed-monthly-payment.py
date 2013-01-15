# given variables
balance = 10000
annualInterestRate = .2

# set variables
tempBalance = balance
monthlyInterestRate = annualInterestRate / 12
payment = 0

while tempBalance > 0:
    
    # reset balance if this while loop has not met the condition
    tempBalance = balance

    # set payment increment
    payment += 10
    
    for month in range(1,13):
        newBalance = (tempBalance - payment)*(1 + monthlyInterestRate)
        tempBalance = newBalance
    
print('Lowest Payment: ' + str(round(payment, 2)))
