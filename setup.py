#!/usr/bin/env python

import argparse
from distutils.command.install import install as _install
from distutils.core import setup
import os
import sys

DATAROOTDIR = 'share'
SYSCONFDIR = 'etc'
MANDIR = os.path.join(DATAROOTDIR, 'man')
MAN1DIR = os.path.join(MANDIR, 'man1')

data_files = [
    (MAN1DIR, ['doc/picgp.1']),
    # This list should be completed with the file picgp.conf
]

class install(_install):
    """Specialized Python source installer."""
    user_options = _install.user_options + [
        ('sysconfdir=', None,
            'Specify the path where to install configuration files'),
    ]
    def initialize_options(self, *args, **kwargs):
        _install.initialize_options(self, *args, **kwargs)
        self.sysconfdir = SYSCONFDIR
    def finalize_options(self, *args, **kwargs):
        _install.finalize_options(self, *args, **kwargs)
        data_files.append((self.sysconfdir, ['data/picgp.conf']))

setup(
    cmdclass={'install': install},
    name='picgp',
    version='0.1.0',
    description='PIC microcontrollers program loader using the Linux GPIO',
    author='Antonio Serrano Hernandez',
    author_email='toni.serranoh@gmail.com',
    url='https://github.com/aserranoh/picgp',
    license='GPLv3',
    platforms=['Linux',],
    requires=['intelhex'],
    scripts=['bin/picgp'],
    data_files=data_files,
)

