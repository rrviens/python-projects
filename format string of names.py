def namelist(names):
    names_added = []
    for i in names:
        names_added.append(i["name"])
    if len(names_added) <= 1:
        output = ("").join(names_added)
    else:
        output = " & ".join([", ".join(names_added[:-1]),names_added[-1]]) #
    print(output)

#  if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
#                                 names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''


namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}])