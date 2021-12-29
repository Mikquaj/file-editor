from colorama import Fore
import os
import sys,time

logo = """
  ______ _ _                 _ _ _             
 |  ____(_) |               | (_) |            
 | |__   _| | ___    ___  __| |_| |_ ___  _ __ 
 |  __| | | |/ _ \  / _ \/ _` | | __/ _ \| '__|
 | |    | | |  __/ |  __/ (_| | | || (_) | |   
 |_|    |_|_|\___|  \___|\__,_|_|\__\___/|_|   
                                               
                                               """
        
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

def animacja():
    animacja = ["|", "/", "-", "\\"]

    for x in range(5):
        for i in animacja:
            print(Fore.RED + 'Ładowanie...' + Fore.BLUE, i)
            os.system('clear')
            time.sleep(0.01)

def start():
    animacja()
    time.sleep(0.5)
    os.system("clear")
    print(Fore.BLUE + logo)
    time.sleep(2)
    sprint(Fore.BLUE + "Co chcesz zrobić?\n\n1. Zapisać plik\n\n2. Odczytać plik\n\n3. Wyczyścić plik\n\n0. Wyjść\n")
    time.sleep(1)
    sprint(Fore.YELLOW + "Wybierz opcje: " + Fore.WHITE)
    wybor = int(input(""))

    cyfry = [1, 2, 3, 0]

    if wybor == 1:
        zapisz()

    if wybor == 2:
        odczytaj()

    if wybor == 3:
        wyczysc()

    if wybor == 0:
        sprint(Fore.RED + "okej")
        time.sleep(1)
        exit()

    if wybor != cyfry:
        sprint(Fore.RED + "Zła opcja!")
        time.sleep(1)
        os.system("clear")
        start()

def zapisz():
    wybor = input(Fore.CYAN + "\nŚcieżka do pliku: " + Fore.WHITE)
    if os.path.exists(wybor):

        f = open(wybor, "a") 
        tekst = input(Fore.CYAN + "\nTekst: " + Fore.WHITE)
        f.write("\n" + tekst)
        f.close()
        time.sleep(1)
        start()
    else:
        sprint(Fore.RED + "\nNie znaleziono pliku")
        time.sleep(5)
        start()

def odczytaj():
    wybor = input(Fore.CYAN + "\nŚcieżka do pliku: " + Fore.WHITE)
    if os.path.exists(wybor):
        with open(wybor) as f:
            for line in f:
                sprint(line)
            time.sleep(1)
            start()    
    else:
        sprint(Fore.RED + "\nNie znaleziono pliku")
        time.sleep(5)
        start()

def wyczysc():
    wybor = input(Fore.CYAN + "\nŚcieżka do pliku: " + Fore.WHITE)
    if os.path.exists(wybor):
        plik = open(wybor,"w")
        plik.close()
        sprint(Fore.BLUE + "\nWyczyszczono plik!")
        time.sleep(5)
        start()
    else:
        sprint(Fore.RED + "\nNie znaleziono pliku")
        time.sleep(5)
        start()
start()