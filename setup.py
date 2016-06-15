# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="textart",

    version="1.0.0b",

    description="A package for drawing art-text with similar functionality to pygame",
    long_description=long_description,

    url='github',

    author="Billyoyo",
    author_email="billyoyo@hotmail.co.uk",

    license="MIT"

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],

    keywords="text ascii art render",

    py_modules=["textart"],

)
