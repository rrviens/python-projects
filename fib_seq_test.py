import math
from decimal import *
def gr():
    return (1+math.sqrt(5))/2
def calc(n):
    a = round((math.pow(gr(),n-math.pow((-gr()),-n)))/math.sqrt(5))
    return a



def productFib(prod):
    fib_list = []
    result = []
    n = 1
    while True:
        z = prod / calc(n)
        print("Z", Decimal(z))
        if z in fib_list:
            result.append(z)
            result.append(calc(n))
            result.append(True)
            return result
        else:
            if prod < calc(n) * calc(n-1):
                result.append(calc(n-1))
                result.append(calc(n))
                result.append(False)
                return result 
            fib_list.append(calc(n))
            n += 1


productFib(203023208030065646654504166904697594722576)