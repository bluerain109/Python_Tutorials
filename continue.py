#Make a program to loop through and what jerseys are still allowed (for a sports team)
numbersTaken = [2, 5, 12, 13, 17,]

print("Here are the numbers that are still available:")

#to loop through the numbers and check which is available
for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)

#continue goes after the word and goes to the next iteration useful for skipping additional code

#break means to break out of the loop completely

