# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 22:20:24 2018

@author: zhang
"""

def get_month_num(annual_salary, portion_saved):
    total_cost = 1000000
    semi_annual_raise = 0.07
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    
    month_count = 0
    
    while current_savings <= ((portion_down_payment * total_cost) - 100):
        current_savings *= (1 + r / 12)
        current_savings += portion_saved * annual_salary / 12
        month_count += 1
        if (month_count % 6) == 0:
            annual_salary *= (1 + semi_annual_raise)
    
    return month_count
    

annual_salary = (int)(input("Enter your annual salary: "))

min_savings = (float)(0)
max_savings = (float)(1.0)

guess = (min_savings + max_savings) / 2
step = 0
month_need = 0

if get_month_num(annual_salary, max_savings) > 36:
    print("It is not possible to pay the down payment in three years.")
else:
    while month_need != 36:
        month_need = get_month_num(annual_salary, guess)
        print(step, month_need)
        if month_need < 36:
            max_savings = guess
        else:
            min_savings = guess
        
        guess = (min_savings + max_savings) / 2
        step += 1
    
    print("Best saving rate:", guess)
    print("Steps in bisection search:", step)