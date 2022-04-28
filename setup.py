#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# metadata
"A texture pack tool for the Minecraft: Pi Edition: Reborn mod."
__version__ = "1.1"
__license__ = "AGPLv3+"
__author__ = "mcpiscript"
__email__ = "mcpiscript@gmail.com"
__url__ = "https://github.com/mcpiscript"
__prj__ = "mcpit"

from setuptools import setup


with open("README.md") as file:
    long_description = file.read()

setup(
    name="mcpit",
    version="1.1",
    description="A texture pack tool for the Minecraft: Pi Edition: Reborn mod.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="mcpiscript",
    author_email="mcpiscript@gmail.com",
    maintainer="Alexey Pavlov",
    maintainer_email="pezleha@duck.com",
    url="https://github.com/mcpiscript",
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)"
    ],
    packages=["mcpit"],
    install_requires=["pillow",  "click"],
    package_dir={"mcpit": "src"}, 
    entry_points={
        "console_scripts": ["mcpit = mcpit.__main__:main", "pepack = mcpit.__main__:main"]
    },
)
