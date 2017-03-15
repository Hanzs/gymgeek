# DOMA
nakup = []

for i in range (10):
    nakup.append(input())

print ("Bež na nákup")

# v OBCHODĚ
print("--- OBCHOD ---")
for i in range (len(nakup)):
    zbozi = input (">")

    if zbozi in nakup:
        print ("OK")
        nakup.remove(zbozi)
    else:
        print ("Měl jsi koupit něco jiného")

print("Nekoupil jsi toto:")
for nekoupene_zbozi in nakup:
    print(nekoupene_zbozi)
