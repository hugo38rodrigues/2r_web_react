from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from .table import Privilege, User, Categorie


class Requests_Data_Base:
    def __init__(self, session: sessionmaker):
        self.session: sessionmaker = session

    def add_users(self, users: dict):
        with self.session.begin():
            citoyen_priv: list = self.session.query(Privilege).filter(Privilege.nom == "citoyen").all()
            
            for user in users.values():
                self.session.add(
                    User(nom=user["nom"], prenom=user["prenom"], pseudo=user["pseudo"], mot_de_passe=user["mdp"],
                         date_naissance=user["date"], email=user["email"], id_privilege=citoyen_priv[0].id))

            self.session.commit()

    def get_categorie(self):
        with self.session.begin():
            reponse = self.session.execute(select(Categorie)).fetchall()
            return [res[0] for res in reponse]