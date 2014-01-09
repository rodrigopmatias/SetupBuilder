# -*- coding: utf-8 -*-
import sys
import os

from setuptools import setup, find_packages
from importlib import import_module


def name():
    return '%(project)s'


def version():
    setup_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(setup_dir, 'src')

    sys.path.insert(0, src_dir)
    try:
        module = import_module(name())
    except ImportError:
        return '0.0.0'
    else:
        return getattr(module, '__version__', '0.0.0')


setup(
    version=version(),
    name=name(),
    description='Simples description.',
    long_description='',
    author='Author name',
    author_email='Author public email',
    url='http://pypi.python.org/%(project)s',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[],
)
