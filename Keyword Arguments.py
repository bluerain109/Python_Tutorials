#when no arguments are present, it just uses the default keywords
def dumb_sentence(name='cat', action='ate', item='duck'):
    print(name, action, item)

dumb_sentence()
#by default whenever we pass in parameters, it's going to pass them in the order entered, this references the order of variables using the entered expressions
dumb_sentence("Megan","loves","ducks.")

dumb_sentence(action='eats')
dumb_sentence()

#you can change the values temporarily by redefining the variable inside of the function's variable.