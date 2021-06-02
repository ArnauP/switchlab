#!/usr/bin/env python

import re
from setuptools import setup, find_packages
from distutils.cmd import Command
from sphinx.setup_command import BuildDoc
from pyqt_distutils.build_ui import build_ui
from subprocess import check_call


_version = re.search(r'__version__\s+=\s+\'(.*)\'',
                     open('kb_simulator/__init__.py').read()).group(1)


class BDistAppCommand(Command):
    """ Custom command to build the application. """

    description = 'Build the application'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        check_call(['pyinstaller', '-y', 'switchlab.spec'])


class BInstallerCommand(Command):
    """ Custom command to build windows installer """
    description = 'Generate the application installer'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        check_call(['iscc', 'scripts/inno_setup.iss'])


class BTrCommand(Command):
    """ Custom command to build the Qt translations files. """

    description = 'Build translation files'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        check_call(['pylupdate5', '-verbose', 'resources/swlb.pro'])


class BUISubclassCommand(build_ui):
    def run(self):
        self.run_command('build_tr')
        super().run()


setup(
    name='switchlab',
    version=_version,
    packages=find_packages(),
    description='SwitchLab',
    author='Arnau Plans',
    author_email='contact@arnauplans.com',
    url='https://www.arnauplans.com',
    cmdclass={
        'bdist_app': BDistAppCommand,
        'build_docs': BuildDoc,
        'build_ui': BUISubclassCommand,
        'build_tr': BTrCommand,
        'build_win_installer': BInstallerCommand,
    }, install_requires=['PyQt5']
)
