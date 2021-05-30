# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:49:41 2021

@author: manan
"""

def sort_string(words_string):
    words_list = words_string.split()
    words_list = [word.lower() for word in words_list]
    words_list.sort()
    return " ".join(words_list)
    
print(sort_string("hello manan really well done"))
    
    
#    first_letter = []
#    for index, word in enumerate(words_list):
#        fl_temp = word[0]
#        first_letter.append(fl_temp)
#    first_letter.sort()
        
        