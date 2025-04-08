import re, random
from colorama import Fore, init
init(autoreset=True)
destination={
    "beaches":["Bali", "Maldives","Phuket","Goa","Thailand"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas"],
    "cities":["Tokyo","Paris","New York"]
    
}
jokes=[
    "Why dont programmers like nature? Too many bugs",
    "Why did the computer go to the doctor? Because it had a virus",
    "Why do travellers always feel warm? Because of all their hot spots"
]
def normalise_input(text):
    return re.sub(r"\s+","",text.strip().lower())
def recommend():
    print(Fore.CYAN+"TravelBot:Beaches,mountains, or cities?")
    preference=input(Fore.YELLOW + "You:")
    preference=normalise_input(preference)
    if preference in destination:
        suggestion=random.choice(destination[preference])
        print(Fore.GREEN+"TravelBot:How about{suggestion}?")
        print(Fore.CYAN+"TravelBot:Do you like it?(yes/no)")
        answer=input(Fore.YELLOW+"You:").lower()

        if answer=="yes":
           print(Fore.GREEN+"TravelBot:Awesome, Enjoy {suggestion}")
        elif answer=="no":
            print(Fore.RED+"TravelBot:Lets try another")
            recommend()
        else:
            print(Fore.RED+"TravelBot:I'll suggest again")
            recommend()
    else:
        print(Fore.RED+"TravelBot:Sorry, I dont have that type of destination.")
    show_help()

def packing_tips():
    print(Fore.CYAN+"TravelBot:Where to?")
    location=normalise_input(input(Fore.YELLOW+"You:"))
    print(Fore.CYAN+"TravelBot:How many days?")
    days=input(Fore.YELLOW+"You:")
    
    print(Fore.GREEN+"Packing tips for {days} days in {location}:")
    print(Fore.GREEN+"Pack versatile clothes")
    print(Fore.GREEN+"Bring charger/adapter")
def telljoke():
    print(Fore.YELLOW+"TravelBot:"+random.choice(jokes))
def show_help():
    print(Fore.MAGENTA+"\n1 can:")
    print(Fore.GREEN+"- Suggest travel spots(say recommendation)")
    print(Fore.GREEN+"- Offer packing tips(say packing)")
    print(Fore.GREEN+"Tell a joke( say joke)")
    print(Fore.CYAN+"Type exit to end.\n")
def chat():
    print(Fore.CYAN+"Hello, I'm TravelBot")
    name=input(Fore.YELLOW+"Your name?")
    print(Fore.GREEN+"Nice to meet you"+name)
    show_help()

    while True:
        userinput=input(Fore.YELLOW+name+":")
        userinput=normalise_input(userinput)

        if "recommend" in userinput or "suggest" in userinput:
            recommend()
        elif "pack" in userinput or "packing" in userinput:
            packing_tips()
        elif "joke" in userinput or "funny" in userinput:
            telljoke()
        elif "help" in userinput:
            show_help()
        elif "exit" in userinput:
            print(Fore.CYAN+"TravelBot:Safe travel, goodbye")
            break
        else:
            print(Fore.RED+"TravelBot:Could you rephrase?")
if __name__=="_main_":
    chat()
