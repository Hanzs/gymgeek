def vytvor_sachovnici():
    sachovnice=[]
    for i in range(3):
        sachovnice.append([])
        for policko in range(3):
            sachovnice[i].append(" ")
    return sachovnice
#hraci_plocha=vytvor_sachovnici()
def zobraz_plochu(plocha):
    for radek in plocha:
        print(radek)
#zobraz_plochu(hraci_plocha)
def hra():
    plocha=vytvor_sachovnici()
    player1=True
    for i in range(9):
        zobraz_plochu(plocha)
        if player1==True:
            print("player1's turn")
            radek=int(input("Napiš číslo řádku: "))
            policko=int(input("Napiš číslo sloupce: "))
            plocha[radek-1][policko-1]="X"
            player1=False
        else:
            print("player2's turn")
            radek=int(input("Napiš číslo řádku: "))
            policko=int(input("Napiš číslo sloupce: "))
            plocha[radek-1][policko-1]="O"
            player1=True

hra()
