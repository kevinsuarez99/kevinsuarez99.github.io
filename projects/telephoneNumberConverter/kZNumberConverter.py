#program that asks the user for a 10 character
#telephone number in the format XXX-XXX-XXXX
#the program should display the telephone number with any
#alphabetic character inputed instead of numbers
#if the input is 555-GET-FOOD the program should output 555-438-3663
#the program must handle upper and lower case and "-" or " "

print("""\t"Welcome to telephone Number Converter Program" """)#welcome string

def main(): #main function
    print("\nThe format is: XXX-XXX-XXXX or XXX XXX XXXX")#this shows the user the format that the pc wants the phone number to be inputed
    phoneNum = input("\nPlease enter a 10 charcater telephone number: ")#asks for an input number
    while len(phoneNum) > 12 or len(phoneNum) < 12:#this is to make sure that the phone number is not longer than the input format
        print("The number is too long or too short. Try Again")#if the number is longer, then the pc will prompt the same question again
        phoneNum = input("\nPlease enter a telephone number: ")
    if len(phoneNum) == 12: #if the number is on the correct length and format, it will run the functions to convert it
        newNum = kZNumberConverter(phoneNum)
        print("\nThis is your converted number:")#string to show the user the phone number
        finalNum(newNum)

def kZNumberConverter(x):
    x = x.upper()#it will turn the string to uppercase
    newNum = []#it will also create a new list to add the new converted values
    for ch in x:#then iterate though the values of the inputed number
        if ch in ["A", "B", "C"]:#only thos values of the input that are alphabetic will be translated or looked at
            newNum.append(2)
        elif ch in ["D", "E", "F"]:
            newNum.append(3)
        elif ch in ["G", "H", "I"]:
            newNum.append(4)
        elif ch in ["J", "K", "L"]:
            newNum.append(5)
        elif ch in ["M", "N", "O"]:
            newNum.append(6)
        elif ch in ["P", "Q", "R", "S"]:
            newNum.append(7)
        elif ch in ["T", "U", "V"]:
            newNum.append(8)
        elif ch in ["W", "X", "Y", "Z"]:
            newNum.append(9)
        else:
            newNum.append(ch)#if the value is a number, it will directly be appended to the newly created list
    return newNum #then returns the new list with the translated values

def finalNum(z):#this function takes the newly created list with the already converted values as a parameter
    for item in z:#then it will iterate through the list
        print(item, end="")#and print them in a nice format that is easier for the user to read

main()
print("\n\nGOOD BYEEE!!")#final greeting string
