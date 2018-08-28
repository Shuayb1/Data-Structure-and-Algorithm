
#User Inputs
annual_salary = float(input('Enter your starting annual salary:​ ')) #Your salary for the whole year
portion_saved_percentage = float(input('Enter the percent of your salary to save, as a decimal: ​')) #this is the percentage of what you wishes to save monthly
total_cost = float(input('Enter the cost of your dream home: ​'))    #total cost of the dream home
semi_annual_raise = 0.07

#Variables. All amounts in (#)
current_savings = 0  #the amount that you have saved so far,starting from 0
portion_down_payment = 0.25 * total_cost
r = 0.04 #annual rate
annual_return = (current_savings * r) / 12
monthly_salary = annual_salary / 12
portion_saved = portion_saved_percentage * monthly_salary
time = 0


'''
Iteration(while loop is use here to check and compare the present savings and the portion down payment the buyer wished to buy the house, while doing that, the time is iterating too to know the time it will take to save for the purchase)
and the conditional statement if is used to check on the time every 6months (% tells you if the month, divided by 6 equals 0, that is the every 6months), and then calculate the increment every 6months. 
The print method then output the number of months
'''

while (current_savings <= portion_down_payment):
    current_savings += (current_savings * r / 12) + portion_saved
    time += 1
    if time % 6 == 0:
        monthly_salary = (semi_annual_raise * monthly_salary) + monthly_salary
        portion_saved = monthly_salary * portion_saved_percentage
print('Number of months: %d'%time)




