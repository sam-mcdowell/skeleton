# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='skeleton',
    version='0.1.0',
    description='skeleton module',
    long_description=readme,
    author='nobody',
    author_email='no@body.com',
    packages=find_packages(exclude=('tests', 'docs'))
)

