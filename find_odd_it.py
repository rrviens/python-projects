from collections import Counter as c

def find_it(seq):
    cseq = c(seq)
    try_list = []
    for i in cseq:
        if cseq[i] % 2 != 0:
            try_list.append(i)
            return (int("".join(map(str, try_list))))


find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])

# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i