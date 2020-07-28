from collections import Counter

def isValidWalk(walk):
    c = Counter(walk)
    if len(walk) == 10 and c["n"] == c["s"] and c["w"] == c["e"]: # to get somewhere you need to move back the same amount
        return True
    else: 
        return False


# for i in range(2): # test as many times as you want, just change the number
#     test1 = create_tests(random.randint(0,20))
#     test.assert_equals(isValidWalk(test1[0]),test1[1])