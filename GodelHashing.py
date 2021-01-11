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
import time

start = time.time()

d={'Abu':2,'Til':3,'Ila':5,'Nef':7}

def repOrNoRep(dict,x):
#This produces all permutations with repetitions
    if x: return product(dict,repeat=permLength)
    return permutations(dict)

newD={}
for permLength in range(1,5):
    for names in [c for c in repOrNoRep(d,False)]:  #True = with rep, False = without rep 
        newD[(''.join(list(map(lambda i:names[i],range(permLength)))))]=prod(list(map(lambda i:d[names[i]],range(permLength))))

#Sorted has a keyword of 'key' as an arg. It allows to decide what you want sorted. 
list(map(lambda x:print('{:16}'.format(x),'{:>6}'.format(newD[x])),dict(sorted(newD.items(),key=lambda x:x[1]))))
stop = time.time()
print(stop - start)


"""
TIMES
1-8   = 30.81
1-9  = 121.19
1-10 = 457.55

"""