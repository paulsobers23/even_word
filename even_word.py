"""
Given that an "even word" is a word in which each character appears an even number of times, write a function that takes in a string and returns the minimum number of letters to be removed to make that string an even word.
even_word('aaaa') == 0
even_word('potato') == 2
even_word('aabbbb') == 0
even_word('aaabbbccc') == 3

Problem: "even word" is a word in which **each character appears an even number of times** 
Example: even_word('aaaa') == 0 because there is 4 a's
Example: even_word('potato') == 2 because if you remove p and a all that remains are otto 
Data Structure: str , hash table
Algorithm:
1: Create a hash table to store the number of times I see a letter
2: create a count for removal
3: now check how many times each character appear 
4: if the character appear an odd number of times add to remove count
5: return remove count

"""

def even_word(string):
    char = {}
    remove_count = 0
    for letter in string:
        if letter in char:
            char[letter] += 1
        else:
            char[letter] = 1
    for letter in char:
        if  char[letter] % 2 != 0:
            char[letter] -= 1
            remove_count += 1
    return remove_count
    
print(even_word('aaaa'))
print(even_word('potato'))
print(even_word('aaabbbccc'))