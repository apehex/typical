#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'decorator>=4.3.0',
    'numpy>=1.14.2',
    'sympy>=1.1.1',
    # TODO: put package requirements here
]

setup_requirements = [
    'bumpversion>=0.5.3',
    'Sphinx>=1.4.8',
    'watchdog>=0.8.3',
    'wheel>=0.29.0',
    # TODO(apehex): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'coverage>=4.1',
    'flake8>=2.6.0',
    'pytest>=2.9.2',
    'pytest-runner>=2.11.1',
    'tox>=2.3.1'
    # TODO: put package test requirements here
]

setup(
    name='typical',
    version='0.1.0',
    description="Automate argument validation: type checking, value range, string formats, urls, and more!",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    author="apehex",
    author_email='apehex@protonmail.com',
    url='https://github.com/apehex/typical',
    packages=find_packages(include=['typical']),
    entry_points={
        'console_scripts': [
            'typical=typical.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='typical',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
