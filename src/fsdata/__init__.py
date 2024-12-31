"""
fsdata

fsspec based data mapper

Configuration file `fsdata.ini`

Sample configuration:

[samples]
path = $HOME/samples

"""

import pandas as pd

from functools import lru_cache

from upath import UPath

from .config import read_config
from .utils import check_path


class Collection:
    """collection of data files"""

    def __init__(self, name: str, path: str = None):
        path = check_path(path)
        self.name = name
        self.path = UPath(path)

    def __repr__(self):
        return f"Collection({self.name!r}, {self.path!r})"

    def items(self):
        return [p.stem for p in self.path.glob("*")]

    def load(self, name):
        file = self.path.joinpath(f"{name}.parquet")
        return pd.read_parquet(file.as_uri())
    
    def save(self, name, data):
        file = self.path.joinpath(f"{name}.parquet")
        data.to_parquet(file.as_uri())

    def remove(self, name):
        file = self.path.joinpath(f"{name}.parquet")
        if file.exists():
            file.unlink()
        else:
            raise FileNotFoundError(file)

@lru_cache
def __getattr__(name: str):
    """get collection as attribute"""
    config = read_config()

    if name.islower() and name in config:
        path = config.get(name, "path")
        return Collection(name, path)
    else:
        raise AttributeError(f"module 'fsdata' has no attribute '{name}'")


def __dir__():
    """list collection names"""
    config = read_config()

    result = __all__ + [name.lower() for name in config.sections()]

    return result


__all__ = ["Collection"]
