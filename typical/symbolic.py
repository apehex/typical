# -*- coding: utf-8 -*-

"""
=============
Maths Symbols
=============
"""

from __future__ import division, print_function, absolute_import

import numpy as np
import sympy as smp

from .generic import iterable
from .numeric import numeric
from .typical import checks

#####################################################################
# SYMBOLIC PREDICATES
#####################################################################

@checks
def _symbolic_scalar(x) -> bool:
    """
    Checks whether the input is a symbolic expression ; any class
    derived from sympy core qualify.

    Parameters
    ----------
    x:
        An argument to check.

    Returns
    -------
    out: bool.
        True if the argument is a symbolic expression.
    """
    return numeric(x) or isinstance(x, smp.Expr)

@checks
def symbolic(x) -> bool:
    """
    Checks whether the input is a symbolic expression ; any class
    derived from sympy core qualify.

    ! NOTE !
    Works on iterables.

    Parameters
    ----------
    x:
        An argument to check.

    Returns
    -------
    out: bool.
        True if the argument is a symbolic expression.
    """
    if isinstance(x, dict):
        return bool(all(map(
            _symbolic_scalar,
            x.values())))
    elif isinstance(x, np.ndarray):
        return bool(all(map(
            _symbolic_scalar,
            x.flat)))
    elif iterable(x):
        return bool(all(map(
            _symbolic_scalar,
            x)))
    else:
        return _symbolic_scalar(x)
