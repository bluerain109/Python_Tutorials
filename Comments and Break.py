#break and continue can be put inside of a loop
magicNumber = 25

#Find the magic number game (goes through 100 to see if our number is the magic number)

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number!")
#this makes the current number n display as the magic number if it is the magic number

#break stops the loop once the number or solution is found
        break
    else:
        print(n)

#We just reviewed a decision inside of a loop

#for adding notes that the computer will not execute, use hashtag for a single line, use 3 double or single quotes
'''
this is a comment

#this is also a comment


#to concatenate a string, you add strings together
print("Duck" + "Cat")

#to print a number along with a string, you have to use a comma to separate them
print("bucky",9)
'''

#if you take a number and divide it by 4 and what you have left is 0, the (%) modulus sign is the remainder (if something is left after an uneven division)
'''
12%4
'''
#this would be 0 because there is nothing left in decimal format as 3 goes into 12

#you can work on both sides of anything
'''
for n in range(101):
    if n%4 is 0:
        print(n, "is a multiple of 4!")
    else:
        print(n)
 '''

