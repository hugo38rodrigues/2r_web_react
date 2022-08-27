import os
from pathlib import Path

from bdd import Data_Base

working_directory = Path(__file__).parent
os.chdir(working_directory)

if __name__ == "__main__":
    bdd: Data_Base = Data_Base.get_instance()
    bdd.init_privilege()
