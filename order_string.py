def sum_string(s):
    sum = 0
    for x in s:
        sum += int(x)
    print(sum)
    return sum

def order_weight(strng):
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))
    
    print(result)



#https://stackoverflow.com/questions/13669252/what-is-key-lambda/13669294#targetText=In%20Python%2C%20lambda%20is%20a,returns%20value%20of%20data%2Fexpression.

# split into ints
# add ints together someList = [(1+0+3), etc...]
# map { string[103]:someList[i] }
# sort map from lowest to highest

order_weight("103 123 4444 99 2000")