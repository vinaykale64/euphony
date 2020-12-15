"""Setup script for euphony"""

import re
from setuptools import setup
from pathlib import Path

NAME = "euphony"
HERE = Path(__file__).absolute().parent ## The directory containing this file
META_PATH = Path("euphony") / "__init__.py"
META_FILE = (HERE / META_PATH).read_text()
INSTALL_REQUIRES = (HERE/"requirements.txt").read_text().split("\n")
README = (
    (HERE/"README.rst").read_text()
)

def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


setup(
    name=NAME,
    version=find_meta("version"),
    description=find_meta("description"),
    long_description=README,
    long_description_content_type="text/markdown",
    url=find_meta("url"),
    author=find_meta("author"),
    author_email=find_meta("email"),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["euphony"],
    include_package_data=True,
    install_requires=INSTALL_REQUIRES
)
