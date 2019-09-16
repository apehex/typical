#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'decorator>=4.3',
    'numpy>=1.14',
    'sympy>=1.1', ]

setup_requirements = [
    'bump2version>=0.5',
    'pip>=19.2',
    'pytest-runner',
    'twine>=1.14',
    'watchdog>=0.9',
    'wheel>=0.33',
    'Sphinx>=1.8', ]

test_requirements = [
    'coverage>=4.5',
    'flake8>=3.7',
    'pytest>=4.6',
    'tox>=3.14', ]

setup(
    author="apehex",
    author_email='apehex@protonmail.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description=":straight_ruler: Harden your project with practical tests & debugging as you code.",
    entry_points={
        'console_scripts': [
            'typical=typical.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='typical',
    name='typical',
    packages=find_packages(include=['typical', 'typical.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/apehex/typical',
    version='0.1.0',
    zip_safe=False,
)
