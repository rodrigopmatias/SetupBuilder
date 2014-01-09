# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='setupbuilder',
    description='Command to generate setup for python packages.',
    author='Rodrigo Pinheiro Matias',
    packages=find_packages('src/')
)
