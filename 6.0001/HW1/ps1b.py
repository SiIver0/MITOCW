# This program will determine how long I will have to save to be able to make a down payment on a house, getting user
# inputs for annual salary, portion of salary to be saved, and total cost of the home
annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal ")
total_cost = input("Enter the cost of your dream home: ")
semi_annual_raise = input('Enter the semi-annual raise, as a decimal: ')

current_savings = 0
portion_down_payment = 0.25
# The amount of the house you must pay off in the downpayment (here it i 25%)
r = 0.04
interest_gained = current_savings *(r/12) 
# how much you get from investments, assuming rate r, at the end of each month
monthly_salary = annual_salary / 12
needed_money = portion_down_payment * total_cost 
enough_money = True 
months = 0 
while enough_money:
    months = months + 1 
    current_savings = current_savings + monthly_salary * portion_saved
    interest_gainend = current_savings * r/12
    current_savings = interest_gained + current_savings 
    if months % 6 == 0:
        monthly_salary = monthly_salary *(1.0+ semi_annual_raise) 


    if needed_money <= current_savings:
        enough_money = False
        

print 'Number of months:', months 




