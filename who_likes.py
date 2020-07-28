def likes(names):
    ln = len(names)
    likes_this = " likes this"
    if ln == 0:
        print("no one" + likes_this)
    else:
        if ln == 1:
            print("".join(names) + likes_this)
        elif ln in range (2, 4):
            print(" and ".join([", ".join(names[:-1]), names[-1]]) + likes_this)
        elif ln > 3:
            print(", ".join(names[0:2]) + " and " + str((ln - 2)) + " others" + likes_this)
        

likes([])
likes(['Peter'])
likes(['Max', 'John', 'Mark'])
likes(['Alex', 'Jacob', 'Mark', 'Max'])

# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this', 
#         2: '{} and {} like this', 
#         3: '{}, {} and {} like this', 
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)