# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# SOrellana, 6/8/2022,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Declare variables
fileName = 'EmployeeData.txt'
lstEmployees = []
strChoice = ''

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
lstEmployees = Fp.read_data_from_file(fileName)

# Show user a menu of options
while True:
    Eio.print_menu_items()

# Get user's menu option choice
    strChoice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice == '1':
        Eio.print_current_list_items(lstEmployees)

    # Let user add data to the list of employee objects
    elif strChoice == '2':
        objE = Eio.input_employee_data()
        lstEmployees.append(objE)
        print('Employee', objE.first_name, objE.last_name, 'was added to the list!')

    # let user save current data to file
    elif strChoice == '3':
        isSaved = Fp.save_data_to_file(fileName, lstEmployees)
        if isSaved == True:
            print('Data was saved to a file!')
        else:
            print('Something went wrong!')

    # Let user exit program
    elif strChoice == '4':
        input('Goodbye! Press Enter to end the program.')
        break

    else: print('Please choose only 1 to 4!')

# Main Body of Script  ---------------------------------------------------- #
