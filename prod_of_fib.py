import math

def gr():
    return (1+math.sqrt(5))/2
def calc(n):
    a = round((math.pow(gr(),n-math.pow((-gr()),-n)))/math.sqrt(5))
    return a
def productFib(prod):
    fib_list = []
    n = 1
    while True:
        z = prod / calc(n)
        if z in fib_list:
            print("{} is the product of {} & {}.".format(prod, int(z), calc(n)))
            break
        else:
            if prod < calc(n) * calc(n-1):
                print('{} is not a product of any Fibonacci sequence integers. Closest are {} & {}, which equates {}.'.format(prod, calc(n-1), calc(n), calc(n-1)*calc(n)))
                break
            fib_list.append(calc(n))
            n += 1

productFib(927372692193078999176)
productFib(4895)


# def productFib(prod):
#   a, b = 0, 1
#   while prod > a * b:
#     a, b = b, a + b
#   return [a, b, prod == a * b]