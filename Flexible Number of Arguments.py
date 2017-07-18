#for things like making a calculator where the amount of arguments being added, this will create a flexible amount of arguments by adding an asterisk sign
def add_numbers(*args):
#it's common practice for developers to always name the flexible arguments variable as args
    total = 0
    for a in args:
        total += a
    #+= everytime a is added as an argument, it is added to the total
    print(total)

add_numbers(3)
add_numbers(3, 32)
add_numbers(3,43,5453,354234,463463)


