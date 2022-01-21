def prime(nm):
    count=0
    for i in range(1,nm+1):
        if (nm%i==0):
            count=count+1
    if(count==2):
        print("Its prime number")
    else:      
        print("Its composite number")
        
nm=int(input("Enter the number: "))
prime(nm)

