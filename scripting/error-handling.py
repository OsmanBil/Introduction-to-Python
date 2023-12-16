while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except KeyboardInterrupt:
        print("You cancelled the operation.")
        break
    finally:
        print("Finally, I executed!")





def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")
    
    return(num_each, leftovers)