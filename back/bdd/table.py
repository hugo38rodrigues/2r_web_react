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


"""
class Privilege(Base):
    __tablename__ = "privilege"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Enum(MyEnum.privilege), nullable=False, unique=True)

    def _repr__(self):
        return f"<privilege(Name = {self.name})>"


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, autoincrement=True, primary_key=True)
    pseudo = Column(String(20), unique=True)
    idPrivilege = Column(Integer, ForeignKey("privilege.id", ondelete='CASCADE'), nullable=False)
    mail = Column(String(50), unique=True, nullable=False)
    pw = Column(String(255), nullable=False)
    dateCreated = Column(Date)
    isActive = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"<account(id = {self.idUser}, NoPrivilege = {self.idPrivilege}, Mail = {self.mail}, Pw = {self.pw}, DateCreated = {self.dateCreated}, Active = {self.Active})>"


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"<category(Name = {self.name})>"


class Resource(Base):
    __tablename__ = "resource"

    id = Column(Integer, autoincrement=True, primary_key=True)
    idAccount = Column(Integer, ForeignKey("account.id", ondelete='CASCADE'), nullable=False)
    idCategory = Column(Integer, ForeignKey("category.id", ondelete='CASCADE'), nullable=False)
    dateCreated = Column(Date)
    hashResource = Column(String(40), nullable=False, unique=True)
    title = Column(String(80))
    content = Column(Text)
    exploited = Column(Boolean, nullable=False)
    type = Column(Enum(MyEnum.typeResource), nullable=False)

    def __repr__(self):
        return f"<resource(idAccount = {self.idAccount}, idCategory = {self.idCategory}, DateCreated = {self.dateCreated}, HashResource = {self.hashResource}, Exploited = {self.exploited},Type = {self.type})>"


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, autoincrement=True, primary_key=True)
    idAccount = Column(Integer, ForeignKey("account.id", ondelete='CASCADE'), nullable=False)
    idResource = Column(Integer, ForeignKey("resource.id", ondelete='CASCADE'), nullable=False)
    answer = Column(Integer, ForeignKey("comment.id", ondelete='CASCADE'))
    content = Column(String(255), nullable=False)
    date = Column(DateTime)

    def __repr__(self):
        return f"<comment(id = {self.id}, idAccount = {self.idAccount}, idResource = {self.idResource}, Answer = {self.answer}, Content = {self.content}, Date = {self.date})>"


class Favourite(Base):
    __tablename__ = "favourite"

    idAccount = Column(Integer, ForeignKey("account.id", ondelete='CASCADE'), primary_key=True)
    idResource = Column(Integer, ForeignKey("resource.id", ondelete='CASCADE'), primary_key=True)

    def __repr__(self):
        return f"<favourite(idAccount = {self.idAccount}, idResource = {self.idResource})>"


class Link(Base):
    __tablename__ = "link"

    userOne = Column(Integer, ForeignKey("account.id", ondelete='CASCADE'), primary_key=True)
    userTwo = Column(Integer, ForeignKey("account.id", ondelete='CASCADE'), primary_key=True)
    familyLink = Column(Enum(MyEnum.familyLink))

    def __repr__(self):
        return f"<link(UserOne = {self.userOne}, UserTwo = {self.userTwo}, Family Link = {self.familyLink})>"
"""
