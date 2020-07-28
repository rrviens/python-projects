import re

def unique_in_order(iterable):
    
    c = re.sub(r'(\S)\1+', '\\1', str(iterable))
    if c.isdigit():
        d = list(c)
        d = [int(i) for i in d]
        print(d)
    else:
        print(list(c))

unique_in_order('123777')
unique_in_order('ABCDAB')

#from itertools import groupby

# def unique_in_order(iterable):
#    return [k for (k, _) in groupby(iterable)]


# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result