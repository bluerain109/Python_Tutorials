#when you want a function to make a calculation without a print and store the answer or response to be used later as a variable we use a return statement
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

#to store in a variable, list the variable and expression of the expression here
megans_limit = allowed_dating_age(23)
old_man_withers_limit = allowed_dating_age(57)
print("Megan can date girls", megans_limit, "or older.")
print("Old Man Withers can date girls", old_man_withers_limit, "or older.")
