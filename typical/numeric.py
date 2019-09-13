# -*- coding: utf-8 -*-

"""
==================
Numeric Predicates
==================
"""

from __future__ import division, print_function, absolute_import

import numpy as np

from typical import typecheck

#####################################################################
# NUMERIC PREDICATES
#####################################################################

@typecheck
def _numeric_scalar(x) -> bool:
    """
    Checks a scalar object value against all the numeric types at once :
    int, float, np.float64...

    Parameters
    ----------
    x:
        An argument to check.

    Returns
    -------
    out: bool.
    """
    try:
        float(x)
    except ValueError:
        return False
    except TypeError:
        return False
    else:
        return True

@typecheck
def numeric(x) -> bool:
    """
    Checks an object against all the numeric types at once :
    int, float, np.float64...

    ! NOTE !
    Can be used on array like objects and iterables.

    Parameters
    ----------
    x:
        An argument to check.

    Returns
    -------
    out: bool.
    """
    if isinstance(x, dict):
        return bool(all(map(
            _numeric_scalar,
            x.values())))
    elif isinstance(x, np.ndarray):
        return bool(all(map(
            _numeric_scalar,
            x.flat)))
    elif iterable(x):
        return bool(all(map(
            _numeric_scalar,
            x)))
    else:
        return _numeric_scalar(x)

@typecheck
def _finite_scalar(x) -> bool:
    """
    Checks whether a scalar input is a finite numeric value.

    Parameters
    ----------
    x:
        An argument to check.

    Returns
    -------
    out: bool.
        True when the argument is finite.
    """
    try:
        bool(np.all(np.isfinite(x)))
    except TypeError:
        return False
    else:
        return bool(np.all(np.isfinite(x)))

@typecheck
def finite(x) -> bool:
    """
    Checks whether the input is (composed of) a finite numeric value.

    ! NOTE !
    Can be used on array like objects and iterables.

    Parameters
    ----------
    x:
        An argument to check.

    Returns
    -------
    out: bool.
        True when the argument is finite.
    """
    if isinstance(x, dict):
        return bool(all(map(
            _finite_scalar,
            x.values())))
    elif isinstance(x, np.ndarray):
        return bool(all(map(
            _finite_scalar,
            x.flat)))
    elif iterable(x):
        return bool(all(map(
            _finite_scalar,
            x)))
    else:
        return _finite_scalar(x)
