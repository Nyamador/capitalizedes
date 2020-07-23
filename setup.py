#!/usr/bin/env python

from setuptools import setup

setup(name='capitalizedes',
      version='1.0',
      # list folders, not files
      packages=['capitalizedes',
                'capitalizedes.test'],
      scripts=['capitalizedes/bin/cap_script.py'],
      package_data={'capitalizedes': ['data/cap_data.txt']},
      )