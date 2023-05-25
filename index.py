# Librairie(s) utilisée(s)
from flask import *

# Création d'un objet application web Flask
app = Flask(__name__)
# Création d'une fonction accueillir() associée à l'URL "/"
# pour générer une page web dynamique

@app.route("/")
def penser():
    """Affiche le formulaire pour récupérer le nom"""
    return render_template("votre_nom.html")

@app.route("/a", methods=["POST"])
def a():
    """Affiche le formulaire pour récupérer le personnage"""
    # Récupération du nom à partir du formulaire
    nom_utilisateur = request.form["nom"]
    # code Admin
    if request.form["nom"] == "Admin":
        return render_template("congratulations.html",nom=nom_utilisateur)
    else:
    # On retourne le template en lui passant les paramètres
        return render_template("perso_choix.html",nom=nom_utilisateur)

@app.route("/mettre")
def mettre():
    """Affiche le formulaire pour récupérer le personnage"""
    # On retourne le template en lui passant les paramètres
    return render_template("sun.html")

@app.route("/indice")
def indice():
    """Affiche un message bonjour"""
    # On retourne le template en lui passant les paramètres
    return render_template("moon.html")

@app.route("/ici")
def ici():
    """Affiche un message bonjour"""
    # On retourne le template en lui passant les paramètres
    return render_template("twig.html")

@app.route("/bien_joue")
def bienjoue():
    """Affiche un message bonjour"""
    # On retourne le template en lui passant les paramètres
    return render_template("bonchoix.html")

def renseigner():
    """Affiche la page a-propos"""
    return "Application web BONJOUR v0.2"

# Lancement de l'application web et son serveur
# accessible à l'URL : http://127.0.0.1:1664
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, debug=True)