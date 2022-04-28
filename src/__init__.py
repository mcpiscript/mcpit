"""
This file is part of mcpit.

mcpit is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

mcpit is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with mcpit. If not, see <https://www.gnu.org/licenses/>.
"""

from zipfile import ZipFile
import os
import shutil

import click

from . import weaving

USER = os.getenv("USER")


INDEX = [
    # Armor
    "chain_1.png",
    "chain_2.png",
    "cloth_1.png",
    "cloth_2.png",
    "diamond_1.png",
    "diamond_2.png",
    "gold_1.png",
    "gold_2.png",
    "iron_1.png",
    "iron_2.png",
    # Miscelannous
    "kz.png",
    "clouds.png",
    # Font and GUI
    "default8.png",
    "background.png",
    "bg32.png",
    "cursor.png",
    "default_world.png",
    "gui.png",
    "gui2.png",
    "gui_blocks.png",
    "icons.png",
    "itemframe.png",
    "items.png",  # Items
    "pi_title.png",
    "spritesheet.png",
    "title.png",
    "touchgui.png",
    "minecon140.png",
    "raknet_high_72.png",
    "raknet_low_18.png",
    # Item entitites
    "arrows.png",
    "camera.png",
    "sign.png",
    # Mobs
    "chicken.png",
    "cow.png",
    "creeper.png",
    "pig.png",
    "pigzombie.png",
    "sheep.png",
    "sheep_fur.png",
    "skeleton.png",
    "spider.png",
    "zombie.png",
    # Misc entities
    "particles.png",
    # Blocks
    "terrain.png",
]

TEXTURE_PATHS = [
    "armor/chain_1.png",
    "armor/chain_2.png",
    "armor/cloth_1.png",
    "armor/cloth_2.png",
    "armor/diamond_1.png",
    "armor/diamond_2.png",
    "armor/gold_1.png",
    "armor/gold_2.png",
    "armor/iron_1.png",
    "armor/iron_2.png",
    "art/kz.png",
    "environment/clouds.png",
    "font/default8.png",
    "gui/background.png",
    "gui/bg32.png",
    "gui/cursor.png",
    "gui/default_world.png",
    "gui/gui.png",
    "gui/gui2.png",
    "gui/gui_blocks.png",
    "gui/icons.png",
    "gui/itemframe.png",
    "gui/items.png",
    "gui/pi_title.png",
    "gui/spritesheet.png",
    "gui/title.png",
    "gui/touchgui.png",
    "gui/badge/minecon140.png",
    "gui/logo/raknet_high_72.png",
    "gui/logo/raknet_low_18.png",
    "item/arrows.png",
    "item/camera.png",
    "item/sign.png",
    "mob/chicken.png",
    "mob/cow.png",
    "mob/creeper.png",
    "mob/pig.png",
    "mob/pigzombie.png",
    "mob/sheep.png",
    "mob/sheep_fur.png",
    "mob/skeleton.png",
    "mob/spider.png",
    "mob/zombie.png",
    "particles.png",
    "terrain.png",
]


def pepack_install(zip_path):
    """
    Install a PePack pack.
    
    Parameters:
    -----------------
    * zip_path
        Path to the ZIP file.
    """
    with ZipFile(zip_path) as zip_file:
        zip_file.extractall(path=f"/home/{USER}/.minecraft-pi/overrides/")


def mcpit_install(zip_path,  interactive=False):
    """
    Install a mcpit pack.
    
    Parameters:
    -----------------
    * zip_path
        Path to the ZIP file.
    * interactive
        This just prints out the credits and the pack changelog if these two files are present. Not sure how this works, but be careful, keep this option off.
    """
    not_found = list()
    found = list()
    with ZipFile(zip_path) as zip_file:
        for file in zip_file.namelist():
            if file in INDEX:
                found.append(file)
            else:
                not_found.append(file)

        for file in found:
            zip_file.extract(
                file,
                path=f"/home/{USER}/.minecraft-pi/overrides/images/"
                + TEXTURE_PATHS[INDEX.index(file)][: -len(INDEX[INDEX.index(file)])],
            )

        if "changelog" in zip_file.namelist():
            with zip_file.open("changelog") as file:
                if interactive: click.echo(file.read())
        if "credits" in zip_file.namelist():
            with zip_file.open("credits") as file:
                if interactive: click.echo(file.read())


def install_pack(zip_path, pack_format,  interactive=False):
    """
    Install a pack.
    
    Parameters:
    -----------------
    * zip_path
        The path to the zip, a string.
    * pack_format
        Can be either ``"mcpit"`` or ``"pepack"``.
    * interactive
        This just prints out the credits and the pack changelog if these two files are present. Not sure how this works, but be careful, keep this option off.
    """
    if pack_format == "mcpit":
        mcpit_install(zip_path,  interactive)
    elif pack_format == "pepack":
        pepack_install(zip_path)


def erase_pack():
    """
    Remove the ``overrides/images` folder.
    """
    shutil.rmtree(f"/home/{USER}/.minecraft-pi/overrides/images")
    
__all__ = ["install_pack",  "mcpit_install",  "pepack_install",  "erase_pack",  "TEXTURE_PATHS",  "INDEX",  "weaving"]
