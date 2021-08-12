("&")
("&")

from getpass import getpass

mot = getpass("Entrez votre mot ")

liste = []
votre_liste = []

for x in mot:
    liste.append(x)
    votre_liste.append('*')

print("".join(votre_liste))

nbr_error = 0
while nbr_error < 9:
    lettre = input("entrez votre lettre:  ")

    if len(lettre) > 1:
        if lettre == mot:
            print("\nVous avez trouvé")
            break
    if lettre in liste:
        for (index, x) in enumerate(liste):
            if x == lettre:
                votre_liste[index] = x
        v = "".join(votre_liste)
        print("Bonne lettre", v)

        if liste == votre_liste:
            print("\nVous avez trouvé le mot")
            break
    else:
        nbr_error += 1
        print("\nMauvaise lettre, il vous reste %s essai(s)"%(9-nbr_error))

if nbr_error == 9:
    print("Vous avez perdu, vous avez epuisé le nombre totale d'essais \nLe mot à trouvé était " + mot + ".")
