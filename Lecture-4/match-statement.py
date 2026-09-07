"""
1- Monday 
2- Tuesday 
... 
7- Sunday 
"""
day_number = int(input("Enter the day number (1-7): "))
match day_number: 
    # this are mutually exclusive cases 
    # i.e, only one executes 
    case 1:
        print("Monday")
    case 2: # same as day_number == 2
        print("Tuesday")
    case 3: 
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5: 
        print("Friday")
    case 6:
        print("Saturday")
    case 7: 
        print("Sunday")
    case _ : # default case else statement 
        # _ is a wild card it matches any value 
        # you need pass this default case at the end 
        print("Invalid day number")