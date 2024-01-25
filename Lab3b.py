#1
import string

def is_anagram(str1, str2):
    def clean_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)

    return sorted(cleaned_str1) == sorted(cleaned_str2)

string1 = 'parliament'
string2 = 'partial men'

if is_anagram(string1, string2):
    print(string1, 'is an anagram of', string2)
else:
    print(string1, 'is not an anagram of', string2)
#2
def is_hexadecimal(str):
    try:
        int_value = int(str, 16)
        return True, int_value
    except ValueError:
        return False, None

def main():
    user_input = input('Enter a string: ')

    is_hex, decimal_value = is_hexadecimal(user_input)

    if is_hex:
        print('The corresponding base-10 value is: ',decimal_value)
    else:
        print('Error: The input is not a valid hexadecimal string.')
if __name__ == "__main__":
    main()

