# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 22:15:39 2018

@author: zhang
"""

annual_salary = (int)(input("Enter your annual salary: "))
portion_saved = (float)(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = (int)(input("Enter the cost of your dream home: "))
semi_annual_raise = (float)(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

month_count = 0

while current_savings <= (portion_down_payment * total_cost):
    current_savings *= (1 + r / 12)
    current_savings += portion_saved * annual_salary / 12
    month_count += 1
    if (month_count % 6) == 0:
        annual_salary *= (1 + semi_annual_raise)

print("Number of months:", month_count)