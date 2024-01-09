import random
from colorama import init , Fore , Style


init()
blue = Fore.BLUE
red = Fore.RED
bold = Style.BRIGHT
print(f"{blue}{bold}Welcome to the {__file__}{Style.RESET_ALL}")

print()
chance = [i for i in range(0,101)]

U_Name = input("Your name: ")
P_Name = input("Your partner name: ")
l = random.choice(chance)
if l<=25:
    v_bad = input("There is very bad result are you want to see: ")
    v_bad.lower()
    if v_bad =="yes":
        print(l)
    else:
        print("As your wish")

elif l>25 and  l<60:
    bad =input("Result is not too good are you want to see")
    bad.lower()
    if bad =="yes":
        print(l)
    else:
        print("As your wish")
    
elif l>60 and  l<75:
    good =input("Result is good are you want to see")
    good.lower()
    if good =="yes":
        print(l)
    else:
        print("As your wish")
else:
    print(f"{blue}{bold}Your chances is too high: {l}")
    