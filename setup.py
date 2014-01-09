# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    version='0.0.1',
    name='setupbuilder',
    description='Command to generate setup for python packages.',
    author='Rodrigo Pinheiro Matias',
    author_email='rodrigopmatias@gmail.com',
    url='http://pypi.python.org/setupbuilder',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'setupbuilder = setupbuilder:main'
        ]
    }
)
