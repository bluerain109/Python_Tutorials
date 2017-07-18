#whenever we make a big computer program, it's good to break your program up into manageable chunks called functions

#you can write a certain bit of code into a function that can easily be reused

#whenever you make a function, write def and then give it a variable name
def duck():
    print("conducktion ducktion what's your function~")

#whenever you actually want to use a function that you created, type the name of the function and then the parentheses after
duck()
#you can use a function over and over again, as many times as you want to call a function means to use a function
duck()
duck()
duck()

#another naming convention aside from doing wordSecondword is word_second_word

#converts a bitcoin amount to USD, how much 1 bitcoin is worth

#inside the parentheses you put the extra information--throw in a variable

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)
#for putting a value inside of a function
duck()
bitcoin_to_usd(3.85)
bitcoin_to_usd(1)
bitcoin_to_usd(13)


