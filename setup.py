#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='nothilfe_tracker',
      version='0.1',
      description='A tracker for the einmalzahlung200.de counters',
      author='Jonas Neubürger',
      author_email='jonas.neubuerger005@stud.fh-dortmund.de',
      packages=find_packages(include=['src', 'src.*']),
      python_requires='>=3.11.2',
     )