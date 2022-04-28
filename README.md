# mcpit

This is the new location for Planet's built-in mcpit's source code. 

## Installation
#### Prequesites
- Python 3
- Pillow
- `click`
#### Actual installation
- Use `pip3 install mcpit`.

## Usage
```
$ mcpit
Usage: mcpit [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  erase    Erase the pack files
  install  Install a texture pack
  version  Show version and license

$ mcpit install path/to/awesome/pack # installs pack as mcpit
$ mcpit install path/to/awesome/pack -p # installs pack as PePack
$ mcpit erase # erases all the packs
```
