import sys
def convertToBase(num, base):
    newNum = '';
    while num > 0:
        newNum += (str(num % base))
        num /= base

    return int(newNum)
