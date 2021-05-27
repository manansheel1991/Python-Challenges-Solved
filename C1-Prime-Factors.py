# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:15:37 2021

@author: manan
"""

def get_prime_factors(number):
    pf_list = []
    divisor = 2
    while(divisor<=number):
        if number%divisor == 0:
            pf_list.append(divisor)
            number = number/divisor
        else:
            divisor = divisor + 1
    return pf_list

print(get_prime_factors(1200))
    