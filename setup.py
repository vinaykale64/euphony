"""Setup script for realpython-reader"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="acoustic",
    version="0.0.1",
    description="Play music while your code runs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/vinaykale64/acoustic",
    author="Vinay Dinkar Kale",
    author_email="vinaykale64@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["acoustic"],
    include_package_data=True,
    install_requires=[
        'pygame>=2.0.0'
    ]
)