## py_bundler basic usage example
 
This is a basic example with only the python part, without the php part.

The full application skeleton will be published later.

THIS DESCRIPTION IS IN DEVELOPMENT, and may be wrong.

### workflows

- `generate-binaries-1.yml`

Installing from `requirements.txt` packages and caching docker layers.

- `generate-binaries-2.yml`

Invokes `Nuitka` to build standalone binaries, and store them as an artifacts into the workflow result.

After that in your release action file, call `dawidd6/action-download-artifact@v2` to get them.

### requirements.txt

This file is used in `generate-binaries-1.yml` step, it installs all packages specified here.

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
