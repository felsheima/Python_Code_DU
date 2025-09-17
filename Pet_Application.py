# Pet Application
# Allison Felsheim
# Python Programming 

# This assignment required the use of tuples.  

# This part asks for information about each pet up for adoption

pet_type_1 = input('Enter the pet type: ').lower()
pet_sex_1 = input('Enter the pet sex: (male/female) ').lower()
pet_age_1 = int(input('Enter the pet age: '))
pet_vaccinated_1 = input('Enter pet vaccination status: (yes/no) ').lower()

# Had to use this if statement to fulfill my requirment for a boolean. The boolean added onto the beginning of the input statement for pet_vaccinated was not properly executing. 

if pet_vaccinated_1 == "yes":
    vaccinated_1 = True
elif pet_vaccinated_1 == "no":
    vaccinated_1 = False
else:
    print("Invalid input: Please enter yes or no")
    vaccinated_1 = None
    
pet_1 = (pet_type_1, pet_sex_1, pet_age_1, vaccinated_1)
    
pet_type_2 = input('Enter the pet type: ').lower()
pet_sex_2 = input('Enter the pet sex: (male/female) ').lower()
pet_age_2 = int(input('Enter the pet age: '))
pet_vaccinated_2 = input('Enter pet vaccination status: (yes/no) ').lower()

if pet_vaccinated_2 == "yes":
    vaccinated_2 = True
elif pet_vaccinated_2 == "no":
    vaccinated_2 = False
else:
    print("Invalid input: Please enter yes or no")
    vaccinated_2 = None
    
pet_2 = (pet_type_2, pet_sex_2, pet_age_2, vaccinated_2)
    
pet_type_3 = input('Enter the pet type: ').lower()
pet_sex_3 = input('Enter the pet sex: (male/female) ').lower()
pet_age_3 = int(input('Enter the pet age: '))
pet_vaccinated_3 = input('Enter pet vaccination status: (yes/no) ').lower()

if pet_vaccinated_3 == "yes":
    vaccinated_3 = True
elif pet_vaccinated_3 == "no":
    vaccinated_3 = False
else:
    print("Invalid input: Please enter yes or no")
    vaccinated_3 = None
    
pet_3 = (pet_type_3, pet_sex_3, pet_age_3, vaccinated_3)
    
pet_type_4 = input('Enter the pet type: ').lower()
pet_sex_4 = input('Enter the pet sex: (male/female) ').lower()
pet_age_4 = int(input('Enter the pet age: '))
pet_vaccinated_4 = input('Enter pet vaccination status: (yes/no) ').lower()

if pet_vaccinated_4 == "yes":
    vaccinated_4 = True
elif pet_vaccinated_4  == "no":
    vaccinated_4 = False
else:
    print("Invalid input: Please enter yes or no")
    vaccinated_4 = None
    
pet_4 = (pet_type_4, pet_sex_4, pet_age_4, vaccinated_4)
    
pet_type_5 = input('Enter the pet type: ').lower()
pet_sex_5 = input('Enter the pet sex: (male/female) ').lower()
pet_age_5 = int(input('Enter the pet age: '))
pet_vaccinated_5 = input('Enter pet vaccination status: (yes/no) ').lower()

if pet_vaccinated_5 == "yes":
    vaccinated_5 = True
elif pet_vaccinated_5  == "no":
    vaccinated_5 = False
else:
    print("Invalid input: Please enter yes or no")
    vaccinated_5 = None
    
pet_5 = (pet_type_5, pet_sex_5, pet_age_5, vaccinated_5)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This part of my code is asking the user to input what pet they are looking to adopt. 

type_of_pet = str(input("Enter the type of pet you're trying to adopt: ")).lower()

age = int(input("Enter the maximum age of the pet you're looking to adopt: "))

gender = str(input("Enter the gender you're looking for: ")).lower()

# This ensures the input for gender is either male or female
if gender not in ['male','female']: 
    print('Invalid input: Please enter male or female') 
    
vaccinated_input = input("Is the pet vaccinated? (yes/no): ").lower()

if vaccinated_input == "yes":
    vaccinated = True
elif vaccinated_input == "no":
    vaccinated = False
else:
    print("Invalid input: Please enter yes or no")
    vaccinated = None 

pet_application = (type_of_pet, age, gender, vaccinated) 

# This function is used to compare the tuples of all the pets I created and my users input for what kind of pet they wanted to adopt 

def matches(application, pet):
    return (
        application[0] == pet[0] and
        pet[1] == application[2] and
        pet[2] < application[1] and
        application[3] == pet[3]
    )

# This is my default value before the matching logic runs, in the event that there is no pet match 
matched_pet = None

#This is where the matching starts 

if matches(pet_application, pet_1):
    print("Your application matches Pet 1")
    matched_pet = pet_1
elif matches(pet_application, pet_2):
    print("Your application matches Pet 2")
    matched_pet = pet_2
elif matches(pet_application, pet_3):
    print("Your application matches Pet 3")
    matched_pet = pet_3
elif matches(pet_application, pet_4):
    print("Your application matches Pet 4")
    matched_pet = pet_4
elif matches(pet_application, pet_5):
    print("Your application matches Pet 5")
    matched_pet = pet_5
else:
    print("Sorry! Your application does not match any of our pets up for adoption right now.")

# If a pet was matched, proceed with payment
if matched_pet != None:
    adoption_fee = float(input("Enter adoption fee: "))
    toy1_price = float(input("Enter price of toy 1: "))
    toy2_price = float(input("Enter price of toy 2: "))
    food_price = float(input("Enter price of food: "))
    carrier_price = float(input("Enter price of carrier: "))
    discount_percent = float(input("Enter discount percent: "))
    
    # Calculate discounted prices (discount only applies to items, not adoption fee)
    discount_amount = discount_percent / 100
    
    toys_total = toy1_price + toy2_price
    toys_discounted = toys_total - (toys_total * discount_amount)
    
    food_discounted = food_price - (food_price * discount_amount)
    
    carrier_discounted = carrier_price - (carrier_price * discount_amount)
    
    # Calculate total
    total_due = adoption_fee + toys_discounted + food_discounted + carrier_discounted
    
    # Print confirmation
    print("--- Adoption Confirmation ---")
    print("Pet Adopted:", matched_pet)
    print("Charges:")
    print("Adoption Fee: $" + str(adoption_fee))
    print("Toys (after discount): $" + str(round(toys_discounted, 2)))
    print("Food (after discount): $" + str(round(food_discounted, 2)))
    print("Carrier (after discount): $" + str(round(carrier_discounted, 2)))
    print("TOTAL DUE: $" + str(round(total_due, 2)))
    print("Congratulations on your adoption!")
