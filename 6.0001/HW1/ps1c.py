# This program determines the best savings rate based on predertimed values and a user defined starting salary. We want

# to be able to put down a down payment in 36 months
annual_salary = input("Enter your starting salary: ")
total_cost = 1000000
semi_annual_raise = 0.07

savings = 0
portion_down_payment = 0.25
# The amount of the house you must pay off in the downpayment (here it i 25%)
r = 0.04

# how much you get from investments, assuming rate r, at the end of each month
monthly_salary = annual_salary / 12
needed_money = portion_down_payment * total_cost
high = 10000
low = 0
guess = ((high+low)/2) * 0.0001
print guess 
not_enough_money = True
i = 0
# this uses a dank bisection search algorithm, with max number of guesses = 13
while not_enough_money:
    i += 1
    savings = 0
    monthly_salary = annual_salary / 12 
    guess1 = guess*10000 
    for month in range(36):
        interest_gained = savings *( r/12)
        savings = savings +( monthly_salary * guess )
        savings = interest_gained + savings
        if month % 6 == 0 :
            monthly_salary = monthly_salary * (1+semi_annual_raise)
        
    if abs(needed_money - savings) <= 100:
        not_enogh_money = False
        break 
    elif savings > needed_money + 100:
        high = guess * 10000
        guess = ((high + low)/2) * 0.0001

        
    elif savings < needed_money - 100:
        low = guess * 10000
        guess = ((high + low)/2) * 0.0001
    print guess
    guess2 = guess *10000
    guess2 = str(guess2)
    guess1 = str(guess1)
    if guess1[0:3] == guess2[0:3]:
        not_enough_money = True
        break
    if i > 13:
        not_enough_money = False
        print 'Cannot save enough fam'
print guess, '% needed'
print i,'numbers in bisection search'



