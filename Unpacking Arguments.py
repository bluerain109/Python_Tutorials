#how to unpack arguments, this means to
def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

megans_data = [27, 20, 0]

#unpacking an argument list uses an asterisk * to pass each item in one at a time, instead of having to write in all
health_calculator(megans_data[0],megans_data[1],megans_data[2])
#so now it is
health_calculator(*megans_data)