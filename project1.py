import sys, random
from termcolor import colored, cprint
print("\n\n")
print("==================\n")
print(colored("Welcome to my NPC Name Generator!\n", "magenta", attrs=["underline"]))
print("This will help you come up with NPC names!\n")
print("==================")

first = ("Jamie", "John", "Archie", "Theodore", "Griffin", "Arco", "Rachel", "Mary", "Gabriel", "Gilberto", "Ronaldo", "Leo", "Dagon", "Dylan", "Dante", "Emerett", "Elijah", "Kimmy", "Quinn", "Jack", "Norbert", "Everest", "Indiana", "Frederick", "Luke",
         "Bryan", "Kevin")
last = ("Johnson", "Abrams", "Sky", "Pocket", "Alvarez", "Winthrop", "Winters", "Arcon", "Bastion", "Branch", "Hibbing", "Gaunt", "Tweed", "Manshore", "Prescot", "Nelson", "Wolf", "Fall")

while True:
    first_name = random.choice(first)
    last_name = random.choice(last)

    print("\n")

    text = colored("{} {}".format(first_name, last_name), "cyan")
    print(text)
    yes_text = colored("Y", "green")
    no_text = colored("n", "red")
    try_again = input("Would You Like To Try Again? (" + yes_text + "/" + no_text + ")\n")
    if try_again.lower() == 'n':
        break
