#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tradecalc',
    version='0.1.2',
    description="Collection of tools to calculate trading positions",
    long_description=readme + '\n\n' + history,
    author="Torsten Irländer",
    author_email='torsten.irlaender@googlemail.com',
    url='https://github.com/toirl/tradecalc',
    packages=[
        'tradecalc',
    ],
    package_dir={'tradecalc':
                 'tradecalc'},
    entry_points={
        'console_scripts': [
            'tradecalc=tradecalc.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='tradecalc',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
