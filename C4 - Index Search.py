# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:23:58 2021

@author: manan
"""

def index_all(list_to_search, search_number):
    number_indices = []
    list_shortened = list_to_search
    number_indices_final = []
    number_temp = 0
    try:
        for i in range(0, len(list_to_search)):
            if list_shortened[i] == search_number:
                number_index_temp = i
                number_indices.append(number_index_temp)
                list_shortened = list_to_search[number_index_temp:]
                number_temp += number_index_temp
                number_indices_final.append(number_temp)
    
    except IndexError:
        
        print("All searching done!")
    
    except ValueError:
        
        print("Done!")
    
    return number_indices_final

print(index_all([1, 1, 2, 3, 4, 7, 5, 7, 2, 4, 3], 2))
print(index_all([1, 1, 2, 3, 4, 7, 5, 7, 2, 4, 3], 3))
print(index_all([1, 1, 2, 3, 4, 7, 5, 7, 2, 4, 3], 4))
print(index_all([1, 1, 2, 3, 4, 7, 5, 7, 2, 4, 3], 5))
    