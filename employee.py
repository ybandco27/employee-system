def main():
    """
    the main body of the program
    displays each of the choices
    available to the user.
    after making a choice
    the program will validate it
    
    and then if it is valid
    will go to the search
    employees function.
    """
    print("")
    choice=""
    
    search_employees(choice)

    finished=False
    valid=False
    choices=["1", "2", "3", "4"]

    while not valid:   
        while not finished:
            print("\n***MAIN MENU***")
            print("\n1.) Print the full details of an employee from their payroll number.")
            print("2.) Print the full details of an employee from their salary range.")
            print("3.) Print the full details of an employee from their given name.")
            print("4.) Quit the program.")
            
            choice=input("\nPlease select an option: ")
            
            if choice in choices:
                valid=True
                if choice=="4":
                    finished=True
                else:
                    search_employees(choice)
            else:
                print("Invalid input! Please try again.")

def search_employees(choice):
    """
    the search employees function
    of the program will first
    take the choice of the user
    made in the main section
    of the program in order to
    perform the correct calculation
    for searching the employee list
    after the correct calculations
    have been made, the program
    refers to the print employees
    function in order to show
    the user all of the employees
    that relate to the search criteria
    """
    
    employees=load_employees()
    
    valid=False
    found=False
    
    while not valid:
        try:
            if choice=="1":
                payroll=input("\nPlease enter an employee payroll number: ")
                if len(payroll) == 5 and payroll.isdigit() == True:
                    print("")
                    valid=True
                    for employee in employees:
                        if employee[0]==payroll:
                            found=True
                            print_employees(employee)
                
            if choice=="2":
                lower=int(input("\nPlease enter a lower limit for the salary: "))
                upper=int(input("Please enter a upper limit for the salary: "))
                if lower >= 0 and lower < 1000000 and upper > 0 and upper < 1000000:
                    print("")
                    valid=True
                    for employee in employees:
                        salary=int(employee[1])
                        if salary > lower and salary < upper:
                            found=True
                            print_employees(employee)      

            if choice=="3":
                valid=True
                search=input("\nPlease enter an employee full name: ")
                print("")
                for employee in employees:
                    name=(employee[3] + " " + employee[4])
                    if search==name:
                        found=True
                        print_employees(employee)

            if choice=="":
                valid=True
                found=True
                print("")
                for employee in employees:
                    print_employees(employee)

            if valid == True and found==False:
                print("No data found for your search!")
                
        except:
            pass       

def load_employees():
    """
    this is a simple function
    that is used to open the
    employees file and store
    the details for later
    use in the program.
    """
    employees=[]
    
    for each in file:
        employee = each.split(" ")
        employees.append(employee)

    return employees


def print_employees(employee):
    """
    a function that is
    called exclusively
    from the search
    employees body of
    the program...
    this is simply used
    to format the details
    of the employee and
    in turn print them
    to the user.
    """
    result = "{0:30s} {1:5s} {2:15s} £{3:1s}".format(employee[4] + ", " + employee[3], employee[0], employee[2], employee[1])
    result = result.replace("\n", "")
    print(result)     

if __name__ == '__main__':

    """
    the start of the
    program is simply
    used to load the
    employee file
    after this, it will
    then simply call
    the main function
    of the program
    """

    valid=False

    filename=input("\nEnter a filename for the employees file: ")
    
    try:
        file = [line.rstrip('\n') for line in open(filename)]
        valid=True
    except:
        pass

    if valid==True:
        main()
    else:
        print("\nA invalid filename was supplied!")
