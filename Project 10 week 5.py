purchasePrice = float(input("Enter the purchase price: $"))
downPayment = 0.10 * purchasePrice
annualInterest = 0.12
monthlyPaymentPercentage = 0.05
balance = purchasePrice - downPayment
monthlyPayment = monthlyPaymentPercentage * purchasePrice
month = 1
print(f"{'Month':<8}{'Total Balance':<20}{'Interest Owed':<20}{'Principal Owed':<20}{'Payment':<15}{'Balance Remaining':<20}")
print("="*100)
while balance > 0:
    interest = balance * (annualInterest / 12)
    principal = monthlyPayment - interest
    if principal > balance:
        principal = balance
        monthlyPayment = principal + interest
    balanceRemaining = balance - principal
    print(f"{month:<8}{balance:<20.2f}{interest:<20.2f}{principal:<20.2f}{monthlyPayment:<15.2f}{balanceRemaining:<20.2f}")
    balance = balanceRemaining
    month += 1
