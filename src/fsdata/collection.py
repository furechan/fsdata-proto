"""fsdata collection"""

import pandas as pd

from upath import UPath

from .utils import check_path


class Collection:
    """collection of data files"""

    def __init__(self, name: str, path: str):
        path = check_path(path)
        self.name = name
        self.path = UPath(path)

    def __repr__(self):
        return f"Collection({self.name!r}, {self.path!r})"

    def items(self):
        return [p.stem for p in self.path.glob("*.parquet")]

    def load(self, name: str):
        file = self.path.joinpath(f"{name}.parquet")
        return pd.read_parquet(file.as_uri())

    def save(self, name: str, data):
        file = self.path.joinpath(f"{name}.parquet")
        data.to_parquet(file.as_uri())

    def remove(self, name: str):
        file = self.path.joinpath(f"{name}.parquet")
        if file.exists():
            file.unlink()
        else:
            raise FileNotFoundError(file)

