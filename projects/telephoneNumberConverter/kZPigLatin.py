#this program takes a sentence as an input and converts each
#word into pig latin
#the first letter of a word will be removed and placed at the
#end of the word and then append "OX" to the word
#the program should handle uppercase and lowercase
#example, if input = "I SLEPT MOST OF THE NIGHT."
#output should be "I SLEPT MOST OF THE NIGHT."

print("""\t"Welcome to Pig Latin Converter Program" """)#welcome string
#main function
def main():#asks for a string as an input
    str = input("Please enter a sentence string: ")#the input is a sentence
    str = str.upper()#it converts the input alphabet characters to uppercase
    str = str.split(" ")#then splits the string where the " " is located to create a list[] out of it

    kZPigLatin(str)#function called under main

def kZPigLatin(x):#this function is what takes care of the translation to pig latin

    str2 = []#it creates a new list[] so it can add the translated characters/string into it
    for words in x:#iterates through the words that were separated as list items
        for ch in words:#then it iterates through each character in evry word from the list
            if words.index(ch) == 0:#it gets the firt letter of the word and doesnt append it until the end
                fstCH = ch#it instead puts it into a variable
            elif ch == "." or ch == "!" or ch == "?":#if it finds a puntiation point it will ignore it
                continue
            else:
                str2.append(ch)#any other characters will just be appended automatically
        str2.append(fstCH)#it appends that first letter, that was put into a variable before
        str2.append("OX ")#then at the end it appends "OX "
    for item in str2:#finaly it will iterate again through the characters of the new list[] that was created and print
        print(item, end="")#everything as if a normal sentence

main()
print("\nGood Bye!!")#good bye string
