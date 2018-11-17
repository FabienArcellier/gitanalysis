#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='gitanalysis',
    version='1.0.0',
    url='https://github.com/FabienArcellier/gitanalysis',
    author='Fabien Arcellier',
    author_email='fabien.arcellier@gmail.com',
    packages=find_packages(exclude=["*_tests"]),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires = [
        'click',
        'pandas'
    ],
    entry_points = {
        'console_scripts': [
            'gitanalysis = gitanalysis.app.cli:cli',
        ],
    },
    extras_require={
        'dev': [
            'pylint',
            'coverage',
            'tox'
        ]
    }
)
