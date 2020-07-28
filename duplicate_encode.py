from collections import Counter

def duplicate_encode(word):
    # duplicate = []
    # for i in word:
    #     duplicate.append(i)
    #     counter = duplicate.count(i)
    #     print(counter)
    word = word.lower()
    counter = Counter(word) # Counter({'r': 2, 'e': 2, 'd': 2, 't': 1, 'a': 1})
    print(counter)
    ''.join(('(' if counter[c] == 1 else ')') for c in word)

duplicate_encode("retarded")
# solutions:
# 1 
# return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
# 2
# word = word.lower()
# counter = Counter(word)
# return ''.join(('(' if counter[c] == 1 else ')') for c in word)




# i gave up