######print only number from given any string################
def extract_store_sort(string):
    k=[]
    for a in string:
        if a.isalpha()==True:
            k.append(" ")
        if a.isnumeric() == True or a==".":
            k.append(a)        
    s="".join(k)
    k1=s.split()
    lst = list(map(eval, k1))
    print(sorted(lst))
string="AC*wv12n/:#e123we2.45oin  (fwoi6n#a98nfwb+owi"
extract_store_sort(string)

 












