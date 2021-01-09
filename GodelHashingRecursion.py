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
PERMUTATIONS WITH OR WITHOUT REPETITION
"""
from itertools import product,permutations
from math import prod

d={'Abu':2,'Til':3,'Ila':5,'Nef':7}
newD={}

def repOrNoRep(dict,x,permLength):
    if x: return product(dict,repeat=permLength) #This produces all permutations with repetitions
    return permutations(dict) #This produces all permutations without repetitions

def recur(start,end,d,nD,repOrNo):
    if start > end:
        list(map(lambda x:print('{:16}'.format(x),'{:>6}'.format(nD[x])),dict(sorted(nD.items(),key=lambda x:x[1]))))
    else:
        for names in [c for c in repOrNoRep(d,repOrNo,start)]:
            nD[(''.join(list(map(lambda i:names[i],range(start)))))]=prod(list(map(lambda i:d[names[i]],range(start))))
        recur(start+1,end,d,nD,repOrNo)

                #IF FALSE, MAX END = LENGTH OF ORIGINAL DICTIONARY
recur(1,4,d,newD,False) #args= start, end, original dictionary, outputted dictionary, with or without repetitions

