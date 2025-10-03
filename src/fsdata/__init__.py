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

__all__ = ["Collection"]


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
    """list package contents including collection names"""
    config = read_config()

    result = __all__ + [name.lower() for name in config.sections()]

    return result
