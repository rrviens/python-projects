def solution(number):
    add = []
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            add.append(i)
    for n in add:
        sum += n

    print(sum)
solution(10)

#    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)