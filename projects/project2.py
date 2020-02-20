#program that converts from input distance in miles to
#the selected unit desired by user

#   welcome string
print("Welcome to program that converts form miles to a certain unit")
def main():
#   user's input distance in miles
    miles = eval(input("Please eneter the distance in miles: "))

#   choice must be set to zero for the while loop to work
#   it must be set to zero before displayig the menu options
    choice = 0
    while choice != 4:
        menu()
        choice = eval(input("Please eneter your choice: ")) # the user will input their selected option
        if choice == 4:
            print("Bye!") #if the user inputs 4, meaning option 4, the while loop will break and the program will end
            break
#       this are the conversion options
        elif choice == 1:
            print("You have selcted choice 1: convert to kilometers")
            showKilometers(miles)
        elif choice == 2:
            print("You have selected choice 2: convert to inches")
            showInches(miles)
        elif choice == 3:
            print("You have selected choice 3: contert to feets")
            showFeets(miles)
#       this else statement is for the case if the user would input a different value that is not one of the
#       menu options, the program will keep on promting the user untill the user inputs a valuable input
        else:
            print("Invalid input. Please try again")
            miles = eval(input("Please eneter the distance in miles: "))

#   this is the menu function and its content
def menu():
    print("\n\t Menu Options")
    print("1. Convert to kilometers")
    print("2. Convert to inches")
    print("3. Convert to feet")
    print("4. Quit the program")

#   the content for the function named showKilometers
#   it takes charge in the mathematical calculations to convert the input number to km
def showKilometers(miles):
    km = miles * 1.6093
    print(miles, "miles equals >>> {0:0.2f}km <<< ".format(km)) # this will round the result to 2 decimal places

#   the content for the function named showInches
#   it takes charge in the mathematical calculations to convert the input number to inches
def showInches(miles):
    inches = miles * 63360
    print(miles, "miles equals >>> {0:0.2f}in <<< ".format(inches))

#   the content for the function named showFeets
#   it takes charge in the mathematical calculations to convert the input number to feets
def showFeets(miles):
    feet = miles * 5280
    print(miles, "miles equals >>> {0:0.2f}ft <<< ".format(feet))

main()
