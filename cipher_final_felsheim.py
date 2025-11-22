#Allison Felsheim & Morgan Felsheim
#Final Project Ceasar Cipher

#Cipher math portion 
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - start + shift) % 26 + start)
            result += shifted
        else:
            result += char
    return result


class Caesar_Cipher:
    #default shift
    #custom shift
    def __init__(self):
        #instance variables
        self.__default_s = 3
        self.__custom_s = 0

    #the modifiers
    def set_default_s(self, ds):
        self.__default_s = ds

    def set_custom_s(self, cs):
        self.__custom_s = cs

    #accessor methods
    def get_default_s(self):
        return self.__default_s

    def get_custom_s(self):
        return self.__custom_s

    def encrypt_default(self, text):
        #Encrypt using the default shift
        d_shift = 3
        return caesar_cipher(text, self.__default_s)
    
    def encrypt_custom(self, text):
        #Encrypt using the custom shift
        c_shift = int(input('Enter the custom shift you would like for your encryption: '))
        self.__custom_s = c_shift  # Store the custom shift
        return caesar_cipher(text, self.__custom_s)
    
    def decrypt_default(self, text):
        #Decrypt using the default shift
        d_shift = -3
        return caesar_cipher(text, -self.__default_s)
    
    def decrypt_custom(self, text):
        #Decrypt using the custom shift
        c_shift = int(input('Enter the custom shift you would like for your decryption: '))
        self.__custom_s = c_shift  # Store the custom shift
        return caesar_cipher(text, -self.__custom_s)
                

def main():
    print('--------Welcome to our Caesar Cipher program!!--------')
    cipher = Caesar_Cipher()

    history = {} #Store all operations
    entry_count = 1 #keeps track of entries 
    
    while True:
        # Show users how to use the input below
        print("Example Usage: encrypt default")
        print("Example Usage: decrypt custom\n")

        # Ask for the users input- encrypt/decrypt, default/custom
        user_input = input("Please choose encrypt/decrypt, and if you would like to use a default/custom shift. Or type 'exit' to finish: ").lower()

        if user_input == 'exit':
            break
        
        #Check if the user wants to encrypt using the default shift
        elif 'encrypt' in user_input.lower() and 'default' in user_input.lower():
            #Ask the user for the text they want to encrypt
            text = input('Please enter the text you want to encrypt: ')
            #Use the Caesar_Cipher object's method to encrypt the text with the default shift
            result = cipher.encrypt_default(text)
            #print the encrypted text to the user
            print(f'Encrypted text: {result}\n')
            #Store this operation in the history dictionary for reference
            # Key: "Entry {entry_count}", Value: a dictionary with operation type, input, and result
            history[f"Entry {entry_count}"] = {"Operation": "Encrypt (Default)", "Input": text, "Result": result}

        # Check if the user wants to encrypt using a custom shift    
        elif 'encrypt' in user_input.lower() and 'custom' in user_input.lower():
            text = input('Please enter the text you want to encrypt: ')
            # use the encrypt_custom method to encrypt the text with the user's custom shift
            result = cipher.encrypt_custom(text)
            print(f'Encrypted text: {result}\n')
            #Store this operation in the history dictionary for reference
            # Key: "Entry {entry_count}", Value: a dictionary with operation type, input, and result
            history[f"Entry {entry_count}"] = {"Operation": "Encrypt (Custom)", "Input": text, "Result": result}
            
        # Check if the user wants to encrypt using a custom shift
        elif 'decrypt' in user_input.lower() and 'default' in user_input.lower():
            text = input('Please enter the text you want to decrypt: ')
            # use the encrypt_custom method to encrypt the text with the user's custom shift
            result = cipher.decrypt_default(text)
            print(f'Decrypted text: {result}\n')
            #Store this operation in the history dictionary for reference
            # Key: "Entry {entry_count}", Value: a dictionary with operation type, input, and result
            history[f"Entry {entry_count}"] = {"Operation": "Decrypt (Default)", "Input": text, "Result": result}
            
        elif 'decrypt' in user_input.lower() and 'custom' in user_input.lower():
            text = input('Please enter the text you want to decrypt: ')
            # use the encrypt_custom method to encrypt the text with the user's custom shift
            result = cipher.decrypt_custom(text)
            print(f'Decrypted text: {result}\n')
            #Store this operation in the history dictionary for reference
            # Key: "Entry {entry_count}", Value: a dictionary with operation type, input, and result
            history[f"Entry {entry_count}"] = {"Operation": "Decrypt (Custom)", "Input": text, "Result": result}
            
        else:
            print('You did not enter a valid input...please try again...')
            continue

        #Adds for every entry inputed 
        entry_count += 1

        #while loop to determine if user wants to continue or not 
        while True:
            again = input("\nDo you want to encrypt/decrypt another text? (y/n): ").lower()
            if again in ['y', 'n']:
                break
            print("Invalid choice. Please enter 'y' or 'n'.")

        if again == 'n':
            break
        
    # Print final summary
    print("\n=== Summary of All Operations ===")
    if not history:
        print("No operations were performed.")
    else:
        for key, value in history.items():
            print(f"\n{key}:")
            print(f"  Operation: {value['Operation']}")
            print(f"  Input: {value['Input']}")
            print(f"  Result: {value['Result']}")

    print("\nThank you for using the Caesar Cipher program!")
    print("------------------------------------------------")
        
if __name__ == '__main__':
    main()

    
    
