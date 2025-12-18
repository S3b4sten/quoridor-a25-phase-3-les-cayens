"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""

from api import appliquer_un_coup, créer_une_partie, récupérer_une_partie
from quoridor import Quoridor, interpréter_la_ligne_de_commande

# Mettre ici votre IDUL comme clé et votre Jeton comme secret.
JETONS = {
    "CHGAU223": "8f07387e-e832-4251-9c95-4307f520a97f",
}

AUTOMATIQUE = False

if __name__ == "__main__":
    args = interpréter_la_ligne_de_commande()
    secret = JETONS[args.idul]
    id_partie, état = créer_une_partie(args.idul, secret)
    quoridor = Quoridor(
        état["joueurs"],
        état["murs"],
        état["tour"]
        )
    while True:
        print(quoridor)
        if AUTOMATIQUE:#Permet de faire une partie automatiquement si Automatique est à True
            coup, position = quoridor.jouer_un_coup(quoridor.état_partie()["joueurs"][0]["nom"])
        else:
            coup, position = quoridor.sélectionner_un_coup(
                quoridor.état_partie()["joueurs"][0]["nom"]
                )
            coup, position = quoridor.appliquer_un_coup(
                quoridor.état_partie()["joueurs"][0]["nom"],
                coup,
                position,
            )
        try:
            # Envoyer le coup au serveur
            coup, position = appliquer_un_coup(
                id_partie,
                coup,
                position,
                args.idul,
                secret,
            )
            # Appliquer le coup de l'adversaire dans votre jeu
            coup, position = quoridor.appliquer_un_coup(
                quoridor.état_partie()["joueurs"][1]["nom"],
                coup,
                position,
            )
        except StopIteration as erreur:
            id_partie, gagnant_serveur = récupérer_une_partie(
                id_partie,
                args.idul,
                secret,
            )
            quoridor = Quoridor(état["joueurs"], état["murs"], état["tour"])
            print(f"Le gagnant est {str(erreur)}")
            break
