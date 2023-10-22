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
            self.piquet1.append(i+1)
            self.piquet2.append(0)
            self.piquet3.append(0)

        self.piquet1.append(niveau+1)
        self.piquet2.append(niveau+1)
        self.piquet3.append(niveau+1)

    def deplacer_disque(self, num_piquet_depart, num_piquet_arrivee):
        indice_disque_a_prendre = 0
        indice_placement_disque = 0

        #premier cas : piquet1 vers piquet2
        if num_piquet_depart == 1 and num_piquet_arrivee == 2 :
            for i in range(self.niveau):
                if self.piquet1[i] != 0 :
                    indice_disque_a_prendre = i
                    #print(i)
                    break
            for j in range(self.niveau):
                if self.piquet2[j] == 0 and self.piquet2[j+1] != 0 :
                    indice_placement_disque = j
                    #print(j)
                    break

            if self.piquet2[indice_placement_disque+1] > self.piquet1[indice_disque_a_prendre]:
                self.piquet2[indice_placement_disque] = self.piquet1[indice_disque_a_prendre]
                self.piquet1[indice_disque_a_prendre] = 0
                return 0
            else:
                print("Mouvement interdit !")
                return 1

        # deuxieme cas : piquet1 vers piquet3
        if num_piquet_depart == 1 and num_piquet_arrivee == 3 :
            for i in range(self.niveau):
                if self.piquet1[i] != 0 :
                    indice_disque_a_prendre = i
                    #print(i)
                    break
            for j in range(self.niveau):
                if self.piquet3[j] == 0 and self.piquet3[j+1] != 0 :
                    indice_placement_disque = j
                    #print(j)
                    break

            if self.piquet3[indice_placement_disque+1] > self.piquet1[indice_disque_a_prendre]:
                self.piquet3[indice_placement_disque] = self.piquet1[indice_disque_a_prendre]
                self.piquet1[indice_disque_a_prendre] = 0
                return 0
            else:
                print("Mouvement interdit !")
                return 1

        #troisieme cas : piquet2 vers piquet1
        if num_piquet_depart == 2 and num_piquet_arrivee == 1 :
            for i in range(self.niveau):
                if self.piquet2[i] != 0 :
                    indice_disque_a_prendre = i
                    #print(i)
                    break
            for j in range(self.niveau):
                if self.piquet1[j] == 0 and self.piquet1[j+1] != 0 :
                    indice_placement_disque = j
                    #print(j)
                    break

            if self.piquet1[indice_placement_disque+1] > self.piquet2[indice_disque_a_prendre]:
                self.piquet1[indice_placement_disque] = self.piquet2[indice_disque_a_prendre]
                self.piquet2[indice_disque_a_prendre] = 0
                return 0
            else:
                print("Mouvement interdit !")
                return 1

        # quatrieme cas : piquet2 vers piquet3
        if num_piquet_depart == 2 and num_piquet_arrivee == 3 :
            for i in range(self.niveau):
                if self.piquet2[i] != 0 :
                    indice_disque_a_prendre = i
                    #print(i)
                    break
            for j in range(self.niveau):
                if self.piquet3[j] == 0 and self.piquet3[j+1] != 0 :
                    indice_placement_disque = j
                    #print(j)
                    break

            if self.piquet3[indice_placement_disque+1] > self.piquet2[indice_disque_a_prendre]:
                self.piquet3[indice_placement_disque] = self.piquet2[indice_disque_a_prendre]
                self.piquet2[indice_disque_a_prendre] = 0
                return 0
            else:
                print("Mouvement interdit !")
                return 1

        # cinquieme cas : piquet3 vers piquet1
        if num_piquet_depart == 3 and num_piquet_arrivee == 1 :
            for i in range(self.niveau):
                if self.piquet3[i] != 0 :
                    indice_disque_a_prendre = i
                    #print(i)
                    break
            for j in range(self.niveau):
                if self.piquet1[j] == 0 and self.piquet1[j+1] != 0 :
                    indice_placement_disque = j
                    #print(j)
                    break

            if self.piquet1[indice_placement_disque+1] > self.piquet3[indice_disque_a_prendre]:
                self.piquet1[indice_placement_disque] = self.piquet3[indice_disque_a_prendre]
                self.piquet3[indice_disque_a_prendre] = 0
                return 0
            else:
                print("Mouvement interdit !")
                return 1

        # sixieme cas : piquet3 vers piquet2
        if num_piquet_depart == 3 and num_piquet_arrivee == 2 :
            for i in range(self.niveau):
                if self.piquet3[i] != 0 :
                    indice_disque_a_prendre = i
                    #print(i)
                    break
            for j in range(self.niveau):
                if self.piquet2[j] == 0 and self.piquet2[j+1] != 0 :
                    indice_placement_disque = j
                    #print(j)
                    break

            if self.piquet2[indice_placement_disque+1] > self.piquet3[indice_disque_a_prendre]:
                self.piquet2[indice_placement_disque] = self.piquet3[indice_disque_a_prendre]
                self.piquet3[indice_disque_a_prendre] = 0
                return 0
            else:
                print("Mouvement interdit !")
                return 1

    def dessine_piquet(self):
        print("\n",((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", "!", ((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", end=" ")
        print("",((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", "!", ((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", end=" ")
        print("",((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", "!", ((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", end=" \n")

    def dessine_disque(self, niveau_disque):
        if niveau_disque == 0 :
            print("",((int)((self.max_symbole - 1) / 2) + self.espace_init ) * " ", "!", ((int)((self.max_symbole - 1) / 2) + self.espace_init) * " ", end=" ")
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