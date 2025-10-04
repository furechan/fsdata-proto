# Simple data access layer over fsspec

This is a thin abstraction layer over `fsspec` and `universal_pathlib` to access collections of data (dataframes) stored in the file system or in the cloud.

The library reads a config file called `fsdata.ini` which defines a set of collections, each with their own location defined as a valid `fsspec` path.
Each collection acts as a simple container of stored dataframes.

## Configuration

The configuration file `fsdata.ini` has one section for each collection, with the section name as name and with a key `path` pointing to its location. The `path` should be a acceptable `fsspec` path.

```ini
# fsdata.ini

[workspace]
path = ~/Documents/Workspace

[my-samples]
path = S3://my-bucket/my-samples

```

The config file is searched in the `FSDATA_CONFIG_DIRS` environment variable path if defined or otherwize the standard unix config directories, `XDG_CONFIG_HOME` (or ~/.config) and `XDG_CONFIG_DIRS` (or /etc/xdg).

## Usage

To access a given collection just use the `get` method.

```python
# Here `samples` is the name of a collection defined in `fsdata.ini`

import fsdata

samples = fsdata.get("my-sample")
```

To list a collection items
```python
samples.items()
```

Please note that item names do not include any extension.

To load data use the `load` method.

```python
samples.load(name)
```
To save data use the `save` method.

To save data
```python
samples.save(name, data)
```

## Formats

Currently, as a prototype, the library is limited
to pandas dataframes saved in the `parquet` format.


## Installation

You can install the package with `pip`

```
pip install fsdata
```

## Requirements

- universal_pathlib
- pyarrow
- pandas
- fsspec backends like s3fs, etc ... as applicable


## Related Projects and Resources
- [intake](https://github.com/intake/intake) Lightweight package for finding, investigating, loading and disseminating data.
- [pandas](https://github.com/pandas-dev/pandas) Flexible and powerful data analysis / manipulation library for Python
- [pyarrow](https://github.com/apache/arrow) Universal columnar format and multi-language toolbox
- [parquet](https://github.com/apache/parquet-format) Apache Parquet Format
- [fsspec](https://github.com/fsspec/filesystem_spec) Filesystem interfaces for Python
- [universal_pathlib](https://github.com/fsspec/universal_pathlib) pathlib api extended to use fsspec backends
- [pystore](https://github.com/ranaroussi/pystore) Fast data store for Pandas time-series data

