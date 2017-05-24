from random import randrange

print("Hádej číslo, máš 8 pokusů.")

MAX = 100
number = randrange(MAX) + 1
remaining_attempts = 8
guess = None

def get_guess():
    while True:
        n = input("Hádej číslo od 1 do %d: " % MAX)

        if n.isnumeric():
            n = int(n)

            if 1 <= n <= MAX:
                return n
        print("Špatně zadáno")

#Hlavní cyklás - samotné hádání
while remaining_attempts > 0 and guess != number:
    guess = get_guess()
    remaining_attempts -= 1

if guess == number:
    print("VYHRÁL JSI")
else:
    print("PROHRÁL JSI, myslel jsem si číslo %d." % number)
