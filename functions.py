
# Allison Felsheim
# Python Programming Homework 2


def seconds_to_hms(seconds):
    '''This function takes in an argument, seconds (int), and converts it to the following format: xx h, xx m, xx s'''
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours} h, {minutes} m, {seconds} s" 

def miles_to_km(distance):
    '''This funtion takes in an argument, miles, and converts it into kilometers''' 
    return round (distance * 1.6)

def km_to_miles(distance): 
    '''This funtion takes in an argument, kilometers, and converts it into miles''' 
    return round (distance * 0.62)

def europe_us(sqm, euros):
    '''This function converts square meters and euros into dollars and square feet'''
    sqm_conversion_factor = 10.7639
    sqft = round( sqm * sqm_conversion_factor, 2)  
    euro_conversion_factor = 1.08
    dollar = round(euros * euro_conversion_factor, 2)
    return sqft, dollar

def road_trip(mpg):
    '''Calculates total gas cost for a road trip based on mpg and user input distance'''
    distance = float(input('Enter the distance you plan to drive (in miles): '))
    gallons_needed = distance / mpg
    cost_per_gallon = 3.07
    total_cost = round(gallons_needed * cost_per_gallon, 2)
    return total_cost

def insulate_home_cost():
    '''This function takes the length of your basement and converts the total cost of insulation'''
    length = float(input('Enter the length of your basement: '))
    width = float(input('Enter the width of your basement: '))
    height = float(input('Enter the height of your basement: '))
    avg_cost = 2.75
    surface_area_of_walls = 2 *(length * height) + 2 * (width * height)
    total_cost_of_insulation = surface_area_of_walls * avg_cost
    return total_cost_of_insulation


if __name__ == "__main__":
    print('Executing the main part of the script')
    
    seconds_input = int(input('Please enter an amount of seconds you want converted to hours, minutes, seconds: '))
    print('Seconds converted: ', seconds_to_hms(seconds_input))
    print('')
    
    miles_input = float(input('Please enter the miles you want converted to kilometers: '))
    print('Converted to kilometers: ', miles_to_km(miles_input))
    print('')
    
    kilometers_input = float(input('Please enter the kilometers you want converted to miles: '))
    print('Converted to miles: ', km_to_miles(kilometers_input))
    print('')
    
    sqm = float(input('Please enter the number of square meters that you want to convert to square feet: '))
    euros = float(input('Please enter the number of euros you want to convert to US Dollars: '))
    sqft, dollar = europe_us(sqm, euros)
    print(f"That's {sqft} square feet and ${dollar} USD.")
    print('')

    print('Total gas cost for your road trip: ', road_trip(25))
    print('')

    home_insulation = insulate_home_cost()
    print(f'The total cost for your basement insulation is {home_insulation}')
    print('')

    #This line of code is importing my BMI and midpoint function from my extra_functions file within my folder to run a BMI calculator and midpoint number calculator 
    from extra_functions import midpoint

    print('')
    print('Extra functions optional output') 
    midpoint_of_10 = midpoint(10) #Set variable of 10 to find the midpoint of 10 
    print(midpoint_of_10)
    

    
