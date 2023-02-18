member_name=[]
member_password=[]
available_seats=300
display="""
        Seat no: 1-150    ;Rs.75
        Seat no: 151-200  ;Rs.100
        Seat no: 201-250  ;Rs.150"""
seat_no=[i for i in range(1,251)]

def signin(member_name,member_password):
    while True:
        name=input("Username :  ")
        password=input("Create a new password: ")
        if name in member_name:
            print("Please try different name")
        elif password in member_password:
            print("Please try different password")
            
        else:
            member_name.append(name)
            member_password.append(password)
            print("Welcome to Dharshan cinemas")
            print("-----------------------------------------------")
            break

def login(member_name,member_password):
    s=input("Create new account press 1: ")
    if s=="1":
        signin(member_name,member_password)
        while True:
            name=input("Enter your Username:  ")
            password=input("Enter your password: ")
            if name not in member_name or password not in member_password:
                print("Wrong password or name")
            elif member_name.index(name)!=member_password.index(password):
                print("Wrong password or name")
            else:
                print("Logged in successfully")
                print("------------------------------------------------")
                break
    else:
        while True:
            name=input("Enter your Username:  ")
            password=input("Enter your password: ")
            if name not in member_name or password not in member_password:
                print("Wrong password or name")
            elif member_name.index(name)!=member_password.index(password):
                print("Wrong password or name")
            else:
                print("Logged in successfully")
                print("------------------------------------------------")
                break
def booking(available_seats,display,seat_no):
    login(member_name,member_password)
    no_of_seat=int(input("How many seats do you want to book:  "))
    print(display)
    print("-----------------------------------------------")
    print()
    print("Available Seats: ",end=" ")
    for i in seat_no:
        print(i,end=",")
    print()
    seat_start=int(input("Enter the starting seat number: "))
    for j in range(no_of_seat):
        seat_no.remove(seat_start+j)
    if seat_start<=151:
        print("Total = ",no_of_seat*75)
    if seat_start<201 and seat_start>150:
        print("Total = ",no_of_seat*100)
    if seat_start>200:
        print("Total = ",no_of_seat*150)
    print("Your seat has been booked ")
    return seat_no
while True:
    seat_no=booking(available_seats,display,seat_no)
    cont=input("Want to continue press 1")
    if cont!="1":
        break