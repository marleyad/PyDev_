
input1 = input("Please enter a sentence: \n").upper()
print (input1)

input2 = input("Please enter a paragraph: \n").split()
print(f"This is the number of words: {len(input2)}")

input3 = input("Please enter a string so I can check if all characters are digits: ")
if input3.isdigit():
    print("True!\nThe characters are digits!")
else:
    print("False!\nNot all the characters are digits.")

input4 = input("Please enter a string so I can replace 'a' with 'o': ").lower().replace('a', 'o')
print(input4)
        
input5 = input("Please enter your full name (ex. John Smith): ").split()
if len(input5) >= 2:
    print(f"You initials are: {input5[0][0].upper()} {input5[1][0].upper()}")
else:
    print("Please enter at least a first and last name please.")

input6 = len(input("Please enter a string so I can output its length: "))
print(input6)

