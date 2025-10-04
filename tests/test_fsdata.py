import os
import pandas as pd

import fsdata

from fsdata.testing import setup_environment 

setup_environment()


def test_workdir():
    workdir = os.getenv("WORKDIR")
    assert os.path.exists(workdir)

def test_fsdata():
    testdata = fsdata.get("testdata")
    assert isinstance(testdata.items(), list)
    assert isinstance(testdata.load("sample"), pd.DataFrame)

