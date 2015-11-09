balanceCopy = balance
monthlyInterestRate = annualInterestRate/12
payLowBound = balance/12.0
payHighBound = (balance*((1+monthlyInterestRate)**12))/12.0
minPay = 0

while balance > 0.02 or balance < -0.02:
    balance = balanceCopy
    minPay = (payLowBound + payHighBound)/2
    for i in range(12):
        monthlyUnpaid = balance - minPay
        balance = round(monthlyUnpaid + monthlyInterestRate*monthlyUnpaid,2)
    if balance > 0:
        payLowBound = minPay
    if balance < 0:
        payHighBound = minPay

print "Lowest Payment: "+str(round(minPay,2))