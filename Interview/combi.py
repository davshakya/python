import string 
import random 
 
N = 22
res = random.choices(string.ascii_uppercase, k = N)
rndm=''.join(set(res))
print("The generated random string : " + str(rndm)) 
print(len(rndm))
if (len(rndm)==11):
    print("The generated random string : " + str(rndm)) 

