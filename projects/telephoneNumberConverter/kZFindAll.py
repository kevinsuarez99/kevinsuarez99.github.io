#program that takes a string and a substring and calls a
#function that returns the number of instances of the sunstring
#in the substring

#math is imported as it is needed for future calculations
import math

print("""\t "Welcome to Strings Program" """)#welcome string
def main():#main function
    str = input("Please enter a string: ")#it takes an input string
    subStr = input("Now enter a substring: ")#then asks for a substring (the piece of string the user wants to count)

    kZFindAll(str, subStr)#then this function takes in the string and substring as parameters for the
#program to calculate them all


def kZFindAll(x,y):
    chSub = y[0]#it gets the first character of the substring
    if len(y) == 1:#checks if the substring has only a single character
        count = 0
        for i in x:#then it iterates through the string
            if i == chSub:#checks if the value of the variable iterationg through == to that first character of the substring
                count += 1
        print("""\nThere are {} "{}" in the string "{}".""".format(count, y, x))#prints a string with everything the user wanted to know


    elif len(y) == 2:#in the case that the substring would have 2 characters it would do a different operations
        count = 0
        for i in x:#it will iterate just like in the past operations
            if i == chSub:#checks if the the value of the variable iterating == to the substring
                count += 1
        count = count/2#it will the devide the total number count of the first character of the input substring and devide it by 2
        if count % 2 != 0:#this is in the case of getting a decimal number wen deviding by 2
            count = math.floor(count)#it will just round it to the floor number
        print("""\nThere are {} "{}" in the string "{}".""".format(count, y, x))#then it will print a string with the information the user was looking for

main()
print("Goodbye!!")#final greeting string
