# Typical Arguments

> :straight_ruler: Harden your project with practical tests & debugging as you code.

Automate argument validation:
- type checking
- value range (units)
- string formats
- urls validity
- and more!


* Free software: MIT license
* Documentation: https://typical.readthedocs.io.


## Table of Contents

- [Table of Contents](#table-of-contents)
- [Status](#status)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
  - [Future](#future)
  - [History](#history)
  - [Community](#community)
- [Credits](#credits)
- [License](#license)

## Status

[![Development Status][planning-status-shield]](ROADMAP.md)
[![Tagged Release][release-shield]](CHANGELOG.md)
[![Build Coverage][coverage-shield]][coverage-link]

[![Build Status][pypi-shield]][pypi-link]
[![Build Status][travis-shield]][travis-link]
[![Documentation Status][docs-shield]][docs-link]
[![Updates][pyup-shield]][pyup-link]

## Features

You can enfore any predicate validation on your function arguments.

### Type Checking

This module supports type hints as specified by [PEP 484][pep-484] and [PEP 526][pep-526] and implemented in the [typing module][typing-module]. The most fundamental support consists of the types Any, Union, Tuple, Callable, TypeVar, and Generic.

### Unit Checking

Typical can be used in conjunction with unit handling modules like [pint][pint-module].

### Value Range

### String Formats

### URL Validation

### Custom Validation

## Requirements

## Installation

## Usage

## Development

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

### Future

See [ROADMAP](ROADMAP.md)

### History

See [CHANGELOG](CHANGELOG.md)

### Community

See [CODE OF CONDUCT](CODE_OF_CONDUCT.md)

## Credits

See [AUTHORS](AUTHORS.md)

This package was created with [Cookiecutter][cookiecutter] and the custom [cookiecutter-pypackage][cookiecutter-pypackage] project template.

## License

See [LICENSE](LICENSE)

[pep-484]: https://www.python.org/dev/peps/pep-0484
[pep-526]: https://www.python.org/dev/peps/pep-0526
[pint-module]: https://pint.readthedocs.io
[typing-module]: https://docs.python.org/3/library/typing.html

[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter-pypackage]: https://github.com/apehex/cookiecutter-pypackage

[appveyor-shield]: https://ci.appveyor.com/api/projects/status/github/apehex/typical?branch=master&svg=true
[appveyor-link]: https://ci.appveyor.com/project/apehex/typical/branch/master
[coverage-shield]: https://img.shields.io/badge/coverage-0%25-lightgrey.svg?longCache=true
[coverage-link]: https://codecov.io
[docs-shield]: https://readthedocs.org/projects/apehex/badge/?version=latest
[docs-link]: https://typical.readthedocs.io/en/latest/?badge=latest
[pypi-shield]: https://img.shields.io/pypi/v/typical.svg
[pypi-link]: https://pypi.python.org/pypi/typical
[pyup-shield]: https://pyup.io/repos/github/apehex/typical/shield.svg
[pyup-link]: https://pyup.io/repos/github/apehex/typical/
[release-shield]: https://img.shields.io/badge/release-0.1.0-blue.svg?longCache=true
[travis-shield]: https://img.shields.io/travis/apehex/typical.svg
[travis-link]: https://travis-ci.org/apehex/typical

[planning-status-shield]: https://img.shields.io/badge/status-planning-lightgrey.svg?longCache=true
[pre-alpha-status-shield]: https://img.shields.io/badge/status-pre--alpha-red.svg?longCache=true
[alpha-status-shield]: https://img.shields.io/badge/status-alpha-yellow.svg?longCache=true
[beta-status-shield]: https://img.shields.io/badge/status-beta-brightgreen.svg?longCache=true
[stable-status-shield]: https://img.shields.io/badge/status-stable-blue.svg?longCache=true
[mature-status-shield]: https://img.shields.io/badge/status-mature-8A2BE2.svg?longCache=true
[inactive-status-shield]: https://img.shields.io/badge/status-inactive-lightgrey.svg?longCache=true