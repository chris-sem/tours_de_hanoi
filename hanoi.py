def nbre_symbole(n):
    return (5 + (n - 1) * 8)

class TourHanoi:
    niveau = 3
    espace_init = 6
    max_symbole = 0

    piquet1 = []
    piquet2 = []
    piquet3 = []

    def __init__(self, niveau):
        self.niveau = niveau
        self.max_symbole = nbre_symbole(niveau)

        for i in range(niveau):
            self.piquet1.append(i+1);
            self.piquet2.append(0)
            self.piquet3.append(0)

    def dessine_piquet(self):
        print("\n",((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", "!", ((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", end=" ")
        print(((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", "!", ((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", end=" ")
        print(((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", "!", ((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", end=" \n")

    def dessine_disque(self, niveau_disque):
        if niveau_disque == 0 :
            print(((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", "!", ((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", end=" ")
        else :
            n = nbre_symbole(niveau_disque)
            nbre_espace = (int)((self.max_symbole - n) / 2) + self.espace_init
            print("",nbre_espace * " ", n * "=", nbre_espace * " ", end=" ")

    def dessine_socle(self):
        print(((3 * (self.max_symbole + (2 * self.espace_init) + 4) - 2)) * ":")
        print("+", (self.max_symbole + (2 * self.espace_init))*" ","+", (self.max_symbole + + (2 * self.espace_init))*" ","+", (self.max_symbole + + (2 * self.espace_init))*" ","+")
        print(((3 * (self.max_symbole + (2 * self.espace_init) + 4) - 2)) * ":")

    def dessine_jeu(self):

        self.dessine_piquet()

        for i in range(self.niveau):
            self.dessine_disque(self.piquet1[i])
            self.dessine_disque(self.piquet2[i])
            self.dessine_disque(self.piquet3[i])
            self.dessine_piquet()

        self.dessine_socle()