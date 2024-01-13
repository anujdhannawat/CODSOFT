import random
import string

def generate_password(length, complexity):
    if complexity == 'easy':
        characters = string.ascii_letters
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'hard':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose 'easy', 'medium', or 'hard'.")
        return None

    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("CodSoft Password Generator\n")
    length = int(input("Enter the desired length of the password: "))
    
    complexity = input("Choose the complexity level - Easy, Medium, or Hard: ").lower()
    
    password = generate_password(length, complexity)
    
    if password:
        print("Your Generated Password: ", password)

if __name__ == "__main__":
    main()
