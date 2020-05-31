#!/usr/bin/env python

import re
from subprocess import check_call

from setuptools import setup, find_packages, Command

cmdclass = {}

with open('app/__init__.py') as f:
    _version = re.search(r'__version__\s+=\s+\"(.*)\"', f.read()).group(1)


class bdist_app(Command):
    """Custom command to build the application. """

    description = 'Build the application'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        check_call(['./venv/bin/pyinstaller', '-y', 'app.spec'])


cmdclass['bdist_app'] = bdist_app

setup(name='DevRider',
      version=_version,
      packages=find_packages(),
      description='Development Tools',
      author='Namuan',
      author_email='info@bettercallbots.com',
      license='MIT',
      url='https://deskriders.dev',
      entry_points={
          'gui_scripts': ['app=app.__main__:__main__.py'],
      },
      cmdclass=cmdclass)
