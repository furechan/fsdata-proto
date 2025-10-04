"""
fsdata

Collections of data files in a directory or cloud location.
Locations are represendted as local path or valid cloud urls.
Data is saved as parquet files with the extension `.parquet`

Configuration file `fsdata.ini`

Sample configuration:

[samples]
path = $HOME/samples

"""

from functools import lru_cache

from .config import read_config
from .collection import Collection



@lru_cache
def get(name: str) -> Collection:
    """get collection by name"""

    config = read_config()

    if name.islower() and name in config:
        path = config.get(name, "path")
        return Collection(name, path)
    else:
        raise AttributeError(f"module 'fsdata' has no attribute '{name}'")


def items():
    """list available collection names"""

    config = read_config()

    result = [name.lower() for name in config.sections()]

    return result



def __getattr__(name: str):
    """get collection as attribute (legacy! do not use)"""
    return get(name)


def __dir__():
    """list package contents including collection names (legacy! do not use)"""
    return ["Collection"] + items()

