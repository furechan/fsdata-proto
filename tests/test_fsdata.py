import os
import pandas as pd

from pathlib import Path


workdir = Path(__file__).parent.parent
config_dir = workdir.joinpath("tests", "config")

os.environ["WORKDIR"] = workdir.as_posix()
os.environ["XDG_CONFIG_HOME"] = config_dir.as_posix()


def test_workdir():
    workdir = os.getenv("WORKDIR")
    assert os.path.exists(workdir)

def test_fsdata():
    from fsdata import samples
    assert isinstance(samples.items(), list)
    assert isinstance(samples.load("df"), pd.DataFrame)



