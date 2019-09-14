filepath = 'D:/Desktop/Everything/Programming/GitHub/Python Projects/py sorter/sortnumber.txt' # your filepath
with open(filepath) as fp:
    line = fp.readline()
    splitter = line.split(" ")
    splitter = list(map(int, splitter))

splitter.sort()
print(splitter)
