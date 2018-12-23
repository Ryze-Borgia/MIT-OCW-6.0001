# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:43:17 2018

@author: zhang
"""

annual_salary = (int)(input("Enter your annual salary: "))
portion_saved = (float)(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = (int)(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

month_count = 0

while current_savings <= (portion_down_payment * total_cost):
    current_savings *= (1 + r / 12)
    current_savings += portion_saved * annual_salary / 12
    month_count += 1

print("Number of months:", month_count)