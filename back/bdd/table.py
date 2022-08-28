from sqlalchemy import Column, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, primary_key=True)
    nom = Column(String(20), nullable=False)
    prenom = Column(String(20), nullable=False)
    pseudo = Column(String(50), nullable=False, unique=True)
    date_naissance = Column(Date, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    mot_de_passe = Column(String(255), nullable=False)
    id_privilege = Column(Integer, ForeignKey("privilege.id"))


class Privilege(Base):
    __tablename__ = "privilege"
    id = Column(Integer, autoincrement=True, primary_key=True)
    nom = Column(String(30), nullable=False, unique=True)


class Resource(Base):
    __tablename__ = "ressource"
    id = Column(Integer, autoincrement=True, primary_key=True)
    titre = Column(String(50), unique=True, nullable=False)
    date = Column(Date, nullable=False)
    userid = Column(Integer, ForeignKey("user.id"))
    categorieid = Column(Integer, ForeignKey("categorie.id"))


class Categorie(Base):
    __tablename__ = "categorie"
    id = Column(Integer, autoincrement=True, primary_key=True)
    nom = Column(String(30), unique=True, nullable=False)


