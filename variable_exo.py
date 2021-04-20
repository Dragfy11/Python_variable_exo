def main():
    # recolter une valeur port monnaie
    mallet = int(input("Combien as-tu dans ton porte monnaie?"))
    # creer un produit qui aura pour valeur 50
    produit = 50
    # afficher le calcule des 2 valeurs
    total = (mallet - produit)
    # afficher la nouvelle valeur dans le porte feuille
    print("il te reste " + str(total) + " €")


if __name__ == '__main__':
    main()