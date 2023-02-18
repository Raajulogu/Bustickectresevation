# Getting the Limit
t=int(input("Enter the limit:  "))
for i in range(t):
    no_of_t=int(input("Enter the no.of trainees:  "))
    m=input("Give a number for the trainees:  ")
    #Splitting the input(No.for trainees)
    x=m.split(" ")
    #store(number of trainees) as array
    n=[int(j) for j in x]
    for k in range(no_of_t-1):
        k_divisible_by=[]
        for j in range(2,n[k]):
            #storing the nums which is divisible by the k in k_divisible_by
            if n[k]%j==0:
                k_divisible_by.append(j)
        result=0
        for j in k_divisible_by:
            #To check the k has a pair
            if (n[k+1])%j==0:
                result+=1
                break
        if result==1:
            print("Yes")
            print("_______________________________________")
            print()
            break
    else:
        print("No")
        print("_______________________________________")
        print()
            