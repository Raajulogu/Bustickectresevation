member_name=[]
member_password=[]
sino=[]
name=[]
from_=[]
destination=[]
for j in range(20):
    sino.append(j+1)
    name.append("----------")
    from_.append("----------")
    destination.append("----------")
available=20
class members():
    pass
def signin(member_name,member_password):
    while True:
        name=input("Username :  ")
        if name in member_name:
            print("Please try different name")
            continue
        password=input("Create a new password: ")
        if password in member_password:
            print("Please try different password")
            continue
        else:
            member_name.append(name)
            member_password.append(password)
            print("Sign in Successfully ")
            print("Welcome to Dharshan travels")
            print("-----------------------------------------------")
            print()
            break

def login(member_name,member_password):
    signin_option="""Enter:
                    1: Create new account
                    2: Loggin"""
    print(signin_option)
    s=input("")
    if s=="1":
        signin(member_name,member_password)
    else:
        while True:
            name=input("Enter your Username:  ")
            password=input("Enter your password: ")
            if name not in member_name or password not in member_password:
                print("Wrong password or name")
            elif member_name.index(name)!=member_password.index(password):
                print("Wrong password or name")
            else:
                print("Logged in Successfully")
                print("------------------------------------------------")
                break
login(member_name,member_password)
while True:
    def booking(name,from_,destination):
        name_=input("Enter your name: ")
        from__=input("From: ")
        destination_=input("Destination: ")
        sino_=int(input("Enter the seat number: "))
        name[(sino_)-1]=name_
        from_[(sino_)-1]=from__
        destination[(sino_)-1]=destination_
        print("Your seat has been booked")
        print("-------------------------------")
    def cancellation(name,from_,destination):
        sino_=int(input("Enter the seat number: "))
        if name[(sino_)-1]!="----------":
            name[(sino_)-1]="----------"
            from_[(sino_)-1]="----------"
            destination[(sino_)-1]="----------"
            print("Your seat has been cancelled succesfully")
            return 1
        else:
            print("You entered the wrong Seat number")
            print("-------------------------------")
            return 0
        
    def preparechart(sino,name,from_,destination):
        print("SI.NO     Name       From        Destination")
        for i in range(20):
            print(i+1,end="      ")
            print(name[i],end="      ")
            print(from_[i],end="      ")
            print(destination[i])
    def availability(available):
        print(available," Seats available")
    a="""
            1.Booking
            2.Cancellation
            3.Preparechart
            4.Availability
--------------------------------------------------
        """
    print(a)
        
    i=int(input("Please select the option: "))
    if i==1:
        repeat=int(input("How many seats do you want to Book: "))
        for i in range(repeat):
            booking(name,from_,destination)
        available-=repeat
        print("----------------------------------------")
    elif i==2:     
        available+=cancellation(name,from_,destination)
        print("----------------------------------------")
    elif i==3:
        preparechart(sino,name,from_,destination)
        print("----------------------------------------")
    elif i==4:
        availability(available)
        print("----------------------------------------")
    else:
        print("Enter the correct option")
        print("----------------------------------------")
    cont=input("Want to continue press 1: ")
    if cont!="1":
        print("Thank you, Come again")
        break
    else:
        info=input("If you want to logout press 1:  ")
        if info=="1":
            print("Log out Succesfully ")
            print("----------------------------------------")
            login(member_name,member_password)