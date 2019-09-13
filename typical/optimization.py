# -*- coding: utf-8 -*-

"""
=======================
Optimization Algorithms
=======================
"""

from __future__ import division, print_function, absolute_import

import numpy as np

from .typical import typecheck

from .numeric import finite, numeric

#####################################################################
# BOUNDS PREDICATES
#####################################################################

@typecheck
def _check_bounds_tuple(x) -> bool:
    """
    Checks whether a tuple is a valid bound.

    Parameters
    ----------
    x: a tuple.
        Represents the lower and upper bounds.

    Returns
    -------
    out: bool.
        True if the argument is a valid bound tuple.
    """
    is_valid = (
        bool(x) and
        isinstance(x, tuple) and
        len(x) == 2 and
        numeric(x[0]) and
        numeric(x[1]) and
        bool(x[0] <= x[1])) # cast from np.bool_ !!

    return is_valid

@typecheck
def _check_bounds_dict(x) -> bool:
    """
    Checks whether a dict represents valid bounds.

    Parameters
    ----------
    x: dict.
        The argument to check.

    Returns
    -------
    out: bool.
        True if the argument is valid bounds.
    """
    is_valid = (
        bool(x)
        and isinstance(x, dict)
        and all(map(
            lambda t: _check_bounds_tuple(x=t),
            x.values())))
    
    return is_valid

@typecheck
def _check_bounds_array(x) -> bool:
    """
    Checks whether a np.ndarray represents valid bounds.

    Parameters
    ----------
    x: np.ndarray.
        The argument to check.

    Returns
    -------
    out: bool.
        True if the argument is valid bounds.
    """
    is_valid = (
        isinstance(x, np.ndarray)
        and len(x.shape) == 2
        and x.shape[1] == 2
        and all(map(
            lambda t: _check_bounds_tuple(x=t),
            [tuple(line) for line in x])))

    return is_valid

@typecheck
def bounds(x) -> bool:
    """
    Checks whether an argument represents valid bounds.

    Parameters
    ----------
    x:
        The argument to check.

    Returns
    -------
    out: bool.
        True if the argument is valid bounds.
    """
    if isinstance(x, tuple):
        return _check_bounds_tuple(x)
    elif isinstance(x, dict):
        return _check_bounds_dict(x)
    elif isinstance(x, np.ndarray):
        return _check_bounds_array(x)
    else:
        return False

#####################################################################
# SPECIFICATIONS PREDICATES
#####################################################################

@typecheck
def specifications(x) -> bool:
    """
    Checks whether an argument represents valid specifications.

    Parameters
    ----------
    x:
        The argument to check.

    Returns
    -------
    out: bool.
        True if the argument is valid specifications.
    """
    return (
        isinstance(x, dict)
        and bounds(x)
        and all([finite(v[0]) for k, v in x.items()])
        and all([finite(v[1]) for k, v in x.items()]))
