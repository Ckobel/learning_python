import sys
import re

def bin_to_base10(n):
    bin = ""
    while(n > 0):
        bit = n % 2
        quot = n / 2
        bin = str(bit) + bin
        n = quot
    return bin

def max_consecutive_occurence_len(str,occ):
    #takes a string and a value to search within the string
    #returns the maximum number of consecutive occurences within the string
    regex = occ + "+"
    return len(max(re.compile(regex).findall(str)))

n = int(raw_input().strip())
binary_n = bin_to_base10(n)

print max_consecutive_occurence_len(binary_n,"1")
