# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:35:02 2021

@author: manan
"""

def is_palindrome(some_words):
    some_words = some_words.lower()
    some_words = some_words.replace(" ", "")
    l = int(len(some_words)/2)
    for i in range(0, l):
        if some_words[i] == some_words[len(some_words) - i - 1]:
            continue
        else:
            return 0
            break
    return 1

print(is_palindrome("level"))
print(is_palindrome("guttug"))
print(is_palindrome("naman"))
print(is_palindrome("gaggag"))        
        
            
        
        
        
    
    