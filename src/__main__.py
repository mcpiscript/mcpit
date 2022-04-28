#!/usr/bin/env python3
"""
MCPiT: Minecraft Pi Edition Texturepack Tool v.1.1

Copyright (C) 2022  Alexey Pavlov

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
If you would like to obtain a copy of the source code, visit https://github.com/mcpiscript/mcpit
"""

import os
import click

from . import *

USER = os.getenv("USER")


@click.group()
def main():
    pass


@main.command(help="Install a texture pack")
@click.argument("pack_path", type=click.Path(exists=True))
@click.option(
    "--mcpit",
    "-m",
    "pack_format",
    is_flag=True,
    default=True,
    help="Use MCPiT format.",
    flag_value="mcpit",
)
@click.option(
    "--pepack",
    "-p",
    "pack_format",
    is_flag=True,
    default=False,
    help="Use PEPack format.",
    flag_value="pepack",
)
def install(pack_path, pack_format):
    install_pack(pack_path, pack_format,  True)


@main.command(help="Erase the pack files")
def erase():
    erase_pack()


@main.command(help="Show version and license")
def version():
    click.echo(__doc__)


if __name__ == "__main__":
    main()
