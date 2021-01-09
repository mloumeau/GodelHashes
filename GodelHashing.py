# #FOR LOOP MAPS
"""
The first mapping creates a list of all the permutations of n length,
then joins all elements of that list into a single string.
This allocates a new key in the dictionary, entitled with
the name of the string being generated.
""" 

"""
The second mapping does the same, except it accesses the values,
not the keys. Instead of creating a string for these, we get the
product since that is what Godel Hashes do. This end product will
be the value to the string key generated in the first mapping.
"""




"""
PERMUTATIONS WITH REPETITION
"""
from itertools import product,permutations
from math import prod

d={'Abu':2,'Til':3,'Ila':5,'Nef':7}

def repOrNoRep(dict,x):
#This produces all permutations with repetitions
    if x: return product(dict,repeat=permLength)
    return permutations(dict)

newD={}
for permLength in range(1,5):
    for names in [c for c in repOrNoRep(d,True)]:   
        newD[(''.join(list(map(lambda i:names[i],range(permLength)))))]=prod(list(map(lambda i:d[names[i]],range(permLength))))

#Sorted has a keyword of 'key' as an arg. It allows to decide what you want sorted. 
list(map(lambda x:print('{:16}'.format(x),'{:>6}'.format(newD[x])),dict(sorted(newD.items(),key=lambda x:x[1]))))


"""
CRAPPY WAY OF DOING THIS (WITH REPETITION)
"""

# totals={}
# for w in d:
#     totals[w]=d[w]
#     for x in d:
#         totals[x+w]=d[w]*d[x]
#         for y in d:
#             totals[y+x+w] = d[w]*d[x]*d[y]
#             for z in d:
#                 totals[z+y+x+w]=d[w]*d[x]*d[y]*d[z]

# list(map(lambda x:print('{:16}'.format(x),'{:>6}'.format(newD[x])),dict(sorted(newD.items(),key=lambda x:x[1]))))


"""
PERMUTATIONS WITHOUT REPETITION
"""

# from itertools import product, permutations
# from math import prod
# d={'Abu':2,'Til':3,'Ila':5,'Nef':7}
# newD={}
# for permLength in range(1,5):
#     for names in [c for c in list(permutations(d))]:
#         newD[(''.join(list(map(lambda i:names[i],range(permLength)))))]=prod(list(map(lambda i:d[names[i]],range(permLength))))
# list(map(lambda x:print('{:16}'.format(x),'{:>6}'.format(newD[x])),dict(sorted(newD.items(),key=lambda x:x[0]))))