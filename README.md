## py_bundler basic usage example
 
This is a basic example with only the python part, without the php part.

The full application skeleton will be published later.

### workflows

- `generate-binaries.yml`

Installing from `requirements.txt` packages and caching docker layers.

- `publish-release.yml`

Invokes `Nuitka` to build standalone binary.

Publishes(or updates) GA release with binary files using the latest tags from repo.

### requirements.txt

This file is used in `generate-binaries.yml` step, it installs all packages specified here.

Specifying requirements in `TOML` or `cfg` is not supported, and in near future will not be.

### main.py

Nuitka will be called for this file as the entry point for python part.

Probably you should take file from this repository and modify it according to your needs, e.g. add commands
that will be called from php, change description, etc.

### `python` folder

Folder where live python part of your app. You can give it any name you want.

`bundle_info.py` should be the same format in your project as in this repo. Framework use this for bug reports.

It is also recommended to take `log.py` from this repository (just change the logger name inside).

Note: It is not necessary to export anything in `__init__.py`
