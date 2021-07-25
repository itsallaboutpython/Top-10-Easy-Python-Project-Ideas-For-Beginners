import random

def get_random_word_from_wordlist():
    wordlist = []
    with open("hangman_wordlist.txt", 'r') as file:
        wordlist = file.read().split('\n')
    word = random.choice(wordlist)
    return word

def get_some_letters(word):
    letters = []
    temp = '_'*len(word)
    for char in list(word):
        if char not in letters:
            letters.append(char)
    character = random.choice(letters)
    for num, char in enumerate(list(word)):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp

def draw_hangman(chances):
    if chances == 0:
        print("----------")
        print("   ( )-|  ")
        print("  - | -    ")
        print("   / \     ")
    elif chances == 1:
        print("----------")
        print("   ( )-   ")
        print("  - | -    ")
        print("   / \     ")
    elif chances == 2:
        print("----------")
        print("   ( )    ")
        print("  - | -    ")
        print("   / \     ")
    elif chances == 3:
        print("----------")
        print("   ( )    ")
        print("  - | -    ")
        print("   /       ")
    elif chances == 4:
        print("----------")
        print("   ( )    ")
        print("  - | -    ")
        print("           ")
    elif chances == 5:
        print("----------")
        print("   ( )    ")
        print("    |      ")
        print("           ")
    elif chances == 6:
        print("----------")
        print("   ( )    ")
        print("           ")
        print("           ")

def start_hangman_game():
    word = get_random_word_from_wordlist()
    temp = get_some_letters(word)
    chances = 7
    found = False
    while 1:
        if chances == 0:
            print(f"Sorry !!! You Lost, the word was: {word}")
            break
        print("=== Guess the word ===")
        print(temp, end='')
        print(f"\t(word has {len(word)} letters)")
        print(f"Chances left: {chances}")
        character = input("Enter the character you think the word may have: ")
        if len(character) > 1 or not character.isalpha():
            print("Please enter a single alphabet only")
            continue
        else:
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
        if found:
            found = False
        else:
            chances -= 1
        if '_' not in temp:
            print(f"\nYou Won !!! The word was: {word}")
            print(f"You got it in {7 - chances} chances")
            break
        else:
            draw_hangman(chances)
        print()

print("===== Welcome to Hangman Game =====")
while 1:
    choice = input("Do you wanna play hangman (y/n): ")
    if 'y' in choice.lower():
        start_hangman_game()
    elif 'n' in choice.lower():
        print('Exiting...')
        break
    else:
        print("Invalid input...please try again")
    print("\n")