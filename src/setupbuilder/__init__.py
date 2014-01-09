# -*- coding: utf-8 -*-
import sys
import zlib
import base64
import argparse

__version__ = '0.0.1'

__templates = {
    'setup.py': '',
    'MANIFEST.in': '',
    'README.txt': '',
    'LICENSE.txt': '',
    'AUTORS.txt': '',
    'docs': {
        'README.txt': ''
    },
    'tests': {
        'README.txt': ''
    },
    'src': {
        '%(project)s': {
            '__init__.py': ''
        }
    }
}


def ArgumentParser():
    parse = argparse.ArgumentParser()

    parse.add_argument(
        'project'
    )

    parse.add_argument(
        '--with-docs',
        help='',
        dest='docs',
        action='store_true'
    )

    parse.add_argument(
        '--with-tests',
        help='',
        dest='tests',
        action='store_true'
    )

    return parse


def data_compress():
    pass


def main():
    parse = ArgumentParser()

    opts = dict(parse.parse_args().__dict__)
    print(opts)


if __name__ == '__main__':
    main()
