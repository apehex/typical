# -*- coding: utf-8 -*-

"""
===================
Argument Validation
===================

Function decorators to check function arguments and return values against
specified types or predicates.

Examples
--------
    >>> @typecheck
    ... def average(x: int, y:int, z:int) -> float:
    ...     return (x + y + z) / 2
    ...
    >>> average(5.5, 10, 15.0)
    TypeWarning:  'average' method accepts (int, int, int), but was given
    (float, int, float)
    15.25
    >>> average(5, 10, 15)
    TypeWarning:  'average' method returns (float), but result is (int)
    15
"""

from __future__ import division, print_function, absolute_import

from typical.generic import (
	all_of,
    anything,
    exactly,
    iterable,
    nothing,
    one_of)
from typical.iterable import scalar
from typical.numeric import finite, numeric
from typical.optimization import bounds, specifications
from typical.plottable import trace_data
from typical.symbolic import symbolic
from typical.typical import typecheck

__author__ = """David Mougeolle"""
__email__ = 'david.mougeolle@gmail.com'
__version__ = '0.1.0'

__all__ = [
	'all_of',
    'anything',
    'exactly',
    'iterable',
    'nothing',
    'one_of']

__all__ += [
    'scalar']

__all__ += [
	'finite',
	'numeric']

__all__ += [
	'bounds',
	'specifications']

__all__ += [
	'trace_data']

__all__ += [
	'symbolic']

__all__ += [
	'typecheck']
