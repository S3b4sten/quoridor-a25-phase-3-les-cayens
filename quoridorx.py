import turtle
from quoridor import Quoridor

class QuoridorX(Quoridor):

    TAILLE_CASE = 50
    ORIGINE_X = -225
    ORIGINE_Y = -275

    def __init__(self, joueurs, murs=None, tour=1):
        super().__init__(joueurs, murs, tour)

        self.fenetre = turtle.Screen()
        self.fenetre.title("Quoridor")

        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)

        self.afficher()


    def afficher(self):
        self.crayon.clear()
        self.dessiner_entete()
        self.dessiner_damier()
        self.dessiner_coordonnees()
        self.dessiner_pions()
        self.dessiner_murs()
        


    def dessiner_ligne_verticale(self, x):
        self.crayon.penup()
        self.crayon.goto(
            self.ORIGINE_X + x * self.TAILLE_CASE,
            self.ORIGINE_Y
        )
        self.crayon.pendown()
        self.crayon.goto(
            self.ORIGINE_X + x * self.TAILLE_CASE,
            self.ORIGINE_Y + 9 * self.TAILLE_CASE
        )


    def dessiner_ligne_horizontale(self, y):
        self.crayon.penup()
        self.crayon.goto(
            self.ORIGINE_X,
            self.ORIGINE_Y + y * self.TAILLE_CASE
        )
        self.crayon.pendown()
        self.crayon.goto(
            self.ORIGINE_X + 9 * self.TAILLE_CASE,
            self.ORIGINE_Y + y * self.TAILLE_CASE
        )


    def dessiner_damier(self):
        for i in range(10):
            self.dessiner_ligne_verticale(i)
            self.dessiner_ligne_horizontale(i)


    def dessiner_pions(self):
        couleurs = ["blue", "red"]

        for i, joueur in enumerate(self.joueurs):
            x, y = joueur["position"]

            px = self.ORIGINE_X + (x - 0.5) * self.TAILLE_CASE
            py = self.ORIGINE_Y + (y - 0.5) * self.TAILLE_CASE

            self.crayon.penup()
            self.crayon.goto(px, py)
            self.crayon.dot(self.TAILLE_CASE * 0.6, couleurs[i])


    def dessiner_murs(self):
        self.crayon.pensize(5)

        # Murs horizontaux
        for x, y in self.murs["horizontaux"]:
            px = self.ORIGINE_X + (x - 1) * self.TAILLE_CASE
            py = self.ORIGINE_Y + y * self.TAILLE_CASE

            self.crayon.penup()
            self.crayon.goto(px, py)
            self.crayon.pendown()
            self.crayon.goto(px + 2 * self.TAILLE_CASE, py)
        # Murs verticaux
        for x, y in self.murs["verticaux"]:
            px = self.ORIGINE_X + x * self.TAILLE_CASE
            py = self.ORIGINE_Y + (y - 1) * self.TAILLE_CASE

            self.crayon.penup()
            self.crayon.goto(px, py)
            self.crayon.pendown()
            self.crayon.goto(px, py + 2 * self.TAILLE_CASE)

        self.crayon.pensize(1)

    def appliquer_un_coup(self, nom_joueur, coup, position):
        resultat = super().appliquer_un_coup(nom_joueur, coup, position)
        self.afficher()
        return resultat
    

    def dessiner_coordonnees(self):
        self.crayon.penup()
        self.crayon.color("black")

        # Chiffres en bas (x)
        for x in range(1, 10):
            px = self.ORIGINE_X + (x - 0.5) * self.TAILLE_CASE
            py = self.ORIGINE_Y - 25

            self.crayon.goto(px, py)
            self.crayon.write(
                str(x),
                align="center",
                font=("Arial", 12, "normal")
            )

        # Chiffres à gauche (y)
        for y in range(1, 10):
            px = self.ORIGINE_X - 25
            py = self.ORIGINE_Y + (y - 0.5) * self.TAILLE_CASE - 6

            self.crayon.goto(px, py)
            self.crayon.write(
                str(y),
                align="center",
                font=("Arial", 12, "normal")
        )
    

    def dessiner_entete(self):
        self.crayon.penup()
        self.crayon.color("black")

        hauteur_fenetre = self.fenetre.window_height()
        x_depart = self.ORIGINE_X
        y_depart = hauteur_fenetre // 2 - 40

        # Titre
        self.crayon.goto(x_depart, y_depart)
        self.crayon.write(
            "Légende:",
            align="left",
            font=("Arial", 14, "bold")
        )

        # Joueurs
        for i, joueur in enumerate(self.joueurs, start=1):
            texte = (
                f"{i} = {joueur['nom']}, "
                f"murs = {'|' * joueur['murs']}"
            )

            self.crayon.goto(x_depart, y_depart - 25 * i)
            self.crayon.write(
                texte,
                align="left",
                font=("Arial", 12, "normal")
            )