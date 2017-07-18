#a set is a collection of items like a list, except it cannot have any duplicates curly brackets are used
groceries = {'cereal', 'milk','starcrunch','beer','duct tape','lotion','beer'}
print(groceries)
#because of no allowed duplicates in a set, beer will not appear twice

if 'milk' in groceries:
    print('you already have milk! No more is needed at the moment.')
else:
    print('You are out of milk.')

#