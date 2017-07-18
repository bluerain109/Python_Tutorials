#an argument is of more than one variable, to have a default value for an argument. This is useful for web development and a value is required in a database gender profiling
def get_gender(sex="Unknown"):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()

#since no value was put in the final get gender, it resorts to the default value

#if you forget to store the value explicitly, it stores a default value.