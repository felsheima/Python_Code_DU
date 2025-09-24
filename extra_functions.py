#Allison Felsheim
#Python programmg homework_2 extra_functions

def my_func(height, weight):
    '''Calculates BMI from user input'''
    return round(weight * 703 /height /height, 2)


print('---------BMI CALCULATOR---------')
print('')
h = int(input('Please enter your height: (in inches) '))
w = int(input('Please enter your weight: (in pounds) '))
your_BMI = my_func(h, w) 
print(f'Your BMI is {your_BMI}')

#Optional 

def midpoint(number):
    '''Returns the midpoint between the given number and 0'''
    return number / 2

if __name__ == '__main__':
    midpoint_of_10 = midpoint(10)
    print(f'The midpoint of your number is {midpoint_of_10} ')
