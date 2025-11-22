#Final project Ceasar Cipher

class CaesarCipher:
    def __init__(self, default_shift=3):
        # Default shift value can be changed here
        self.default_shift = default_shift

        #Dictionary to store character frequency analysis
        self.frequency_stats = {}

        #List of common cipher shifts to suggest
        self.common_shifts = [1, 2, 5, 13, 25]

        #Tuple of alphabet ranges (immutable configuration)
        self.alphabet_ranges = (
            ('A', 'Z', ord('A')), #Uppercase
            ('a', 'z', ord('a'))  #Lowercase
        )

    def _shift_char(self, char, shift_amount):
        #Use the tuple to determine which alphabet range to use
        for start_char, end_char, base_ord in self.alphabet_ranges:
            if start_char <= char <= end_char:
                return chr((ord(char) - base_ord + shift_amount) % 26 + base_ord)

        #Leave non-letters unchanged
        return char

    def encrypt(self, text, shift=None):
        #Encrypts the text using the Caesar Cipher.
        if shift is None:
            shift = self.default_shift
        result = ""
        for char in text:
            result += self._shift_char(char, shift)

        #Update frequency statistics (dicitionary)
        self._update_frequency(result)
        return result

    def decrypt(self, text, shift=None):
        #Decrypts the text using the Caesar Cipher.
        if shift is None:
            shift = self.default_shift
        result = ""
        for char in text:
            result += self._shift_char(char, -shift)
        return result

    def _update_frequency(self, text):
        #Update character frequency dictionary
        for char in text.upper():
            if 'A' <= char <= 'Z':
                self.frequency_stats[char] = self.frequency_stats.get(char, 0) + 1

    def get_frequency_analysis(self):
        #Returns a list of tuples (char, count) sorted by frequency
        return sorted(self.frequency_stats.items(), key=lambda x: x[1], reverse=True)

    def suggest_shifts(self):
        #Returns a list of common shift values to try
        return self.common_shifts.copy()

    def brute_force_decrypt(self, text):
        #Returns a dictionary of all possible decryptions with their shift values
        results = {}
        for shift in range(26):
            results[shift] = self.decrypt(text, shift=shift)
        return results

    def get_alphabet_info(self):
        #Returns tuple information about alphabet ranges
        return self.alphabet_ranges

    def analyze_text(self, text):
        #Returns a dictionary with various text statistics
        analysis = {'total_chars': len(text), 'letters': 0, 'spaces': 0, 'special': 0, 'char_types': [] }

        for char in text:
            if char.isalpha():
                analysis['letters'] += 1
                analysis['char_types'].append(('letter', char))
            elif char.isspace():
                analysis['spaces'] += 1
                analysis['char_types'].append(('space', char))
            else:
                analysis['special'] += 1
                analysis['char_types'].append(('special', char))

        return analysis 
    
def main():
    # Create a cipher object with a default shift of 3
    cipher = CaesarCipher(default_shift=3)

    #Store encyption history as a list of typles (mode, shift, preview)
    history = []

    while True:
        #Choose inpput method 
        input_mode = input('Read from file or enter text? (type "file" or "text"): ').lower()
            
        #Get text from file or user input
        if input_mode == 'file':
            filename = input('Enter input filename: ')
            try:
                with open(filename, 'r') as f:
                    lines = f.readlines()
                    if not lines:
                        print(f'Error: File {filename} is empty')
                        continue

                    #Remove emppty lines
                    lines = [line.strip() for line in lines if line.strip()]

                    if len(lines) == 0:
                        print(f'Error: File {filename} contains only empty lines')
                        continue

                    #Show all entries in the file
                    print(f'\n-- Contents of {filename} --')
                    for i, line in enumerate(lines, 1):
                        preview = line[:60] + '---' if len(line) > 60 else line
                        print(f'{i}. {preview}')

                    #Ask which entry to process
                    if len(lines) == 1:
                        text = lines[0]
                        print(f'\nProcessing the only entry in file')
                    else:
                        while True:
                            choice = input(f'\nWhich entry do you want to process? (1-{len(lines)} or "all"): ').lower()
                            if choice == 'all':
                                text = '\n'.join(lines)
                                print(f'Processing all {len(lines)} entries together')
                                break
                            elif choice.isdigit() and 1 <= int(choice) <= len(lines):
                                text = lines[int(choice) - 1]
                                print(f'Processing entry {choice}')
                                break
                            else:
                                print(f'Please enter a number between 1 and {len(lines)}, or "all"')
                    print(f"Text selected: '{text[:50]}{'...' if len(text) > 50 else ''}'")
                
            except FileNotFoundError:
                print(f'Error: File "{filename}" not found.')
                continue
            except Exception as e:
                print(f'Error reading file: {e}')
                continue
        elif input_mode == 'text':
            text = input('Enter text: ')
        else:
            print('Please enter "file" or "text".')
            continue

        #Display text analysis
        analysis = cipher.analyze_text(text)
        print(f'\n----Text Analysis---')
        print(f'Total characters: {analysis['total_chars']}')
        print(f"Letters: {analysis['letters']}, Spaces: {analysis['spaces']}, Special Characters: {analysis['special']}")
        
    #Choose encryption or decryption mode 
        while True:
            #Ask user for encrypt, decrypt, or brute-force mode
            mode = input("Type 'e' to encrypt or 'd' to decrypt, or 'b' for brute force decrypt: ").lower()

            #Validate the input
            if mode in ['e', 'd', 'b']:
                break
            else:
                print("Please enter a valid input....")

        #If user selects brute-force decrypt
        if mode == 'b':
            print('\n---Brute Force Decryption (trying all 26 shifts) ---')

            #Call brute-force method which returns all possible shift results 
            results = cipher.brute_force_decrypt(text)

            #Dispaly each shift result with a short preview 
            for shift, decrypted in results.items():
                preview = decrypted[:60] + '...' if len(decrypted) > 60 else decrypted
                print(f'Shift {shift:2d}: {preview}')

            #Ask if they want to save specific result
            save_shift = input('\nEnter shift number to save (or press Enter to skip): ').strip()

            #Check if input is a valid result 
            if save_shift.isdigit():
                shift_num = int(save_shift)

                #Ensure the shift is between 0 and 25
                if 0 <= shift_num <= 25:
                    result = results[shift_num]
                    actual_shift = shift_num
                    operation = 'Brute Force Decrypted'
                else:
                    print('Invalid shfit number.')
                    continue
            else:
                #Ask if user wants to process another input
                again = input('\nDo you want to process another input? (yes/no): ').lower()
                if again != 'yes':
                    print('Goodbye!')
                    break
                continue
        else:
        
            # Choose shift mode for normal encyrption/decryption
            shift_value = None
            while True:
                shift_mode = input("Use default shift or custom? (type 'default' or 'custom'): ").lower()
                if shift_mode == 'default' or shift_mode == 'custom':
                    break
                else:
                    print("Please enter a valid input of 'custom' or 'default'")
        
            #If shift mode is custom, ask user to input shift amount
            if shift_mode == "custom":
                try:
                    shift_value = int(input("Enter custom shift amount: "))
                except ValueError:
                    print('Invalid number. Using default shift instead')
                    shift_value = None
            #If user inputs an invalid number, then default shift takes over
            actual_shift = shift_value if shift_value is not None else cipher.default_shift
    
            # Perform encryption or decryption
            if mode == 'e':
                result = cipher.encrypt(text, shift=shift_value)
                operation = 'Encrypted'
                print("Encrypted text:", result)

                #Show frequency analysis after encryption
                freq_analysis = cipher.get_frequency_analysis()

                #Check if frequency analysis is available 
                if freq_analysis:
                    print('\n--- Character Frequency Analysis (Top 5) ---')

                    #Loop through the top 5 most frequent characters and print them 
                    for char, count in freq_analysis[:5]:
                        print(f'{char}: {count} times')
                
            elif mode == 'd':
                #Decrypt the text using the provided shift value 
                result = cipher.decrypt(text, shift=shift_value)
                operation = 'Decrypted'
                print("Decrypted text:", result)

            else:
                #Handle invalid mode
                print("Invalid mode. Please enter 'e' or 'd'.")
                return
                                
        # Add to history as tuple (operation, shift, text_preview)
        preview = result[:50] + "..." if len(result) > 50 else result
        history.append((operation, actual_shift, preview))

        #Ask if user wants to save to file
        while True:
            save_mode = input('Save result to file? (type "yes" or "no"): ').lower()
            if save_mode == 'yes' or save_mode == 'no':
                break
            else:
                print('Please enter "yes" or "no".')

        if save_mode == 'yes':
            output_filename = input('Enter output filename: ')

            #Ask if they want to append or overwrite
            while True:
                write_mode = input('Append to file or overwrite? (type "append" or "overwrite"): ').lower()

                #Validate user choice
                if write_mode in ['append', 'overwrite']:
                    break
                else:
                    print('Please enter "append" or "overwrite"')
            try:
                #Select file mode: 'a' = append and 'w' = overwrite
                mode_char = 'a' if write_mode == 'append' else 'w'
                #Open the file in the chosen mode
                with open(output_filename, mode_char) as f:
                    #Append a newline before writing only when appending
                    if write_mode == 'append':
                        f.write('\n' + result)
                    else:
                        f.write(result)
                #Confirm action to the user
                action = 'appended to' if write_mode == 'append' else 'saved to'
                print(f'Result {action} {output_filename}')
            except Exception as e:
                print(f'Error writing to file: {e}') 
                                                
        # Display operation history
        if history:
            print("\n=== Operation History ===")

            #List each previous operation with its index
            for i, (op, shift, prev) in enumerate(history, 1):
                print(f"{i}. {op} with shift {shift}: '{prev}'")


        # Ask if user wants to process another input
        again = input('\nDo you want to process another input? (yes/no): ').lower()
        if again != 'yes':
            print('Goodbye!')
            break
        
            
if __name__ == "__main__":
    main()
