# testing module

import os
from pathlib import Path

WORKDIR = Path(__file__).joinpath("../../..").resolve()
CONFIGDIR = WORKDIR.joinpath("tests", "config")

def setup_environment():
    """setup testing enviroment"""
    os.environ["WORKDIR"] = WORKDIR.as_posix()
    os.environ["FSDATA_CONFIG_DIRS"] = CONFIGDIR.as_posix()

