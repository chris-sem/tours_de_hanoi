#On va fixer le nivaeu max à 6

import hanoi

jeu = hanoi.TourHanoi(4)
jeu.dessine_jeu()
jeu.deplacer_disque(1,2)
jeu.dessine_jeu()
jeu.deplacer_disque(1,3)
jeu.dessine_jeu()
jeu.deplacer_disque(2,3)
jeu.dessine_jeu()


