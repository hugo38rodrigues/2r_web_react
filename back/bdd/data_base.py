import pymysql
import sqlalchemy.exc
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
#from sqlalchemy_utils.functions.database import drop_database
#from sqlalchemy.orm import sessionmaker
from .table import Base, Privilege, Categorie
from .requests_data_base import Requests_Data_Base

DEBUG = True


class Data_Base(Requests_Data_Base):

    __instance = None

    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:root@localhost/BDD_2R", echo=True)
        try:
            self.engine.connect()
        except sqlalchemy.exc.SQLAlchemyError:
            print("Pas de BASE DE DONNEE")
            exit(0)


        if DEBUG:
            drop_database(self.engine.url)

        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            Base.metadata.create_all(self.engine)

        self.session = sessionmaker(bind=self.engine)()
        Requests_Data_Base.__init__(Requests_Data_Base, self.session)

    @classmethod
    def get_instance(self):
        if (self.__instance is None):
            self.__instance = Data_Base()
        return self.__instance

    def init_privilege(self):
        with self.session.begin():
            for priv in ["citoyen", "admin"]:
                self.session.add(Privilege(nom=priv))
            try:
                self.session.commit()
            except Exception as e:
                print(e)
                self.session.rollback()

    def init_category(self):
        with self.session.begin():
            for cat in ["bouffe", "sport", "media", "livre"]:
                self.session.add(Categorie(nom=cat))
            try:
                self.session.commit()
            except Exception as e:
                print(e)
                self.session.rollback()
