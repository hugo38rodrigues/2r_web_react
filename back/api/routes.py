from back.bdd import bdd

from flask import Flask

flask_api = Flask(__name__)

@flask_api.get("/")
def home():
    return {"reponse": "OK"}

@flask_api.get("/cat")
def get_categories():
    reponse = bdd.get_categorie()
    return {str(indice): {"nom": cat.nom, "id": cat.id}for indice, cat in enumerate(reponse)}

def run():
    flask_api.run(host="127.0.0.1", port=5000, debug=True)
    
@flask_api.get("/res")
def get_ressources():
    reponse =bdd.get_ressources()
    return {str(indice): {"titre":res.titre, "date":res.date, "id":res.id}for indice,res in enumerate(reponse)}