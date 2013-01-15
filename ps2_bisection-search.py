# given variables
balance = 5000
annualInterestRate = .2

# set variables
tempBalance = balance
monthlyInterestRate = annualInterestRate / 12
payment = 0

# set bounds
lo = balance / 12
hi = (balance * (1 + monthlyInterestRate)**12) / 12

guess = guess = ((hi - lo)/2) + lo

# infinite while loop; break when condition inside is met
while True:

    # reset balance if this while loop has not met the condition
    tempBalance = balance
    guess = ((hi - lo)/2) + lo
    
    # compute balance per guess
    for month in range(1,13):
        newBalance = (tempBalance - guess)*(1 + monthlyInterestRate)
        tempBalance = newBalance

    # our guess was too high
    if tempBalance < -.1:
        hi = guess

    # our guess was too low
    elif tempBalance > 0:
        lo = guess

    # -1 < balance < 0
    else:
        finalBalance = tempBalance
        finalGuess = guess
        break

print('Lowest Payment: ' + str(round(finalGuess, 2)))
