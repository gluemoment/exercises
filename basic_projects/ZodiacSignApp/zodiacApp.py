zodiac_signs_assignment = {
                       0:'Monkey',
                       1:'Rooster',
                       2:'Dog',
                       3:'Pig',
                       4:'Rat',
                       5:'Ox',
                       6:'Tiger',
                       7:'Rabbit',
                       8:'Dragon',
                       9:'Snake',
                       10:'Horse',
                       11:'Goat'
                          }

print("\n")
print("\n")
print("\n")
print("-------------------------------")
print("Welcome to the Zodiac Sign App!")
print("-------------------------------")
print("\n")
print("\n")
print("\n")

def age_input():
    age = input("Please enter your year of Birth?")
    #age = int(age)

    ## Obtaining an input information
    try:
        age = int(age)
    except:
        print('Hey, that was NOT an Integer! Try Again!')

    return age


def finding_zodiac(age, zodiac_signs_assignment):
    zodiac_modulo = age % 12
    # print(zodiac_modulo)
    # print(zodiac_signs_assignment[zodiac_modulo])
    return zodiac_signs_assignment[zodiac_modulo]
    #print(zodiac_modulo)

while True:
    # age = int(input("Please enter your year of Birth?"))
    age = age_input()
    #finding_zodiac(age,zodiac_signs_assignment)
    #finding_zodiac()

    print("\n")
    print("\n")
    print ("So, your Chinese Zodiac Sign is a {}".format(finding_zodiac(age, zodiac_signs_assignment)))
    #finding_zodiac(age,zodiac_signs_assignment))

    print("\n")
    print("\n")
    goAgain = input(f"Play Again? (Press Enter to continue, or q to quit):")
    print("\n")
    print("\n")
    if goAgain == "q":
        break

print("\n")
print("\n")
print("\n")
print('Thanks for Playing! Bye!')
print("\n")
print("\n")
print("\n")
