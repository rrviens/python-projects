def square_digits(num):
    output = []
    for i in str(num):
        output.append(int(i) ** 2)
    get = "".join(map(str, output))

square_digits(9119)

# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)