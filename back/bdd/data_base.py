from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
#from sqlalchemy_utils.functions.database import drop_database
#from sqlalchemy.orm import sessionmaker
from .table import Base, Privilege
#from .ReadFile import *
#from .DbRequest import DbRequest
#from .init.initData import initData

DEBUG = True


class Data_Base:

    __instance = None

    def __init__(self):
        self.engine = create_engine(f"mysql+pymysql://root:root@localhost/BDD_2R", echo=True)

        if DEBUG:
            drop_database(self.engine.url)

        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            Base.metadata.create_all(self.engine)

        self.session = sessionmaker(bind=self.engine)()

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
                self.session.rollback()

