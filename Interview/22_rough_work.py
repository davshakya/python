from itertools import permutations 
your_str ="abcdefghijk"
r=9
print("Input string", your_str) 
permutation = [''.join(x) for x in permutations(your_str,r)]
print(tuple(permutation[1])) 