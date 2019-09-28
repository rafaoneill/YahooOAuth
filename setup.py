#!/usr/bin/env python

import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(name='yahoooauth',
    version=1.0,
    description='Python module to consume Yahoo Fantasy API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rafaoneill/YahooOAuth',
    author='Rafael E. ONeill',
    author_email='rafael.oneill@gmail.com',
    packages=setuptools.find_packages())