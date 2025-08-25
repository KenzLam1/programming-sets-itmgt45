'''Programming Set 1

This assignment will familiarize you with Python's basics.
'''
import math

def savings(gross_pay, tax_rate, expenses):
    return math.floor(gross_pay - (gross_pay * tax_rate) - expenses)

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    waste = total_material - total_consumed
    return f"{waste}{material_units}"

def interest(principal, rate, periods):
    final_amount = principal * (1 + rate * periods)
    return int(final_amount) 


