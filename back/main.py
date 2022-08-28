import os
from pathlib import Path
working_directory = Path(__file__).parent
os.chdir(working_directory)
print("===========================")
print(working_directory)
print("===========================")
from datetime import date
import api
from bdd import bdd


if __name__ == "__main__":

    bdd.init_privilege()
    bdd.init_category()
    
    usersDict: dict[str, dict] = {
        "1": {"nom": "Thomas", "prenom": "NL", "date": date.today(), "pseudo": "DOLIP", "mdp": "1234",
              "email": "tnl.com"},
        "2": {"nom": "Hugo", "prenom": "R", "date": date(2022, 8, 27), "pseudo": "xmls", "mdp": "4321",
              "email": "HR@ro.com"}}
    bdd.add_users(usersDict)


    api.run()