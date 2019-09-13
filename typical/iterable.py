# -*- coding: utf-8 -*-

"""
===================
Iterable Predicates
===================
"""

from __future__ import division, print_function, absolute_import

import numpy as np

from .typical import typecheck

from .generic import iterable

#####################################################################
# MATRIX & ARRAY PREDICATES
#####################################################################

# TODO distinguish the scalar schecking from the numeric checking
# and array can be numeric, but it won't be scalar
# and a scalar can be numeric or not but it won't be array like
@typecheck
def _iterable_scalar(x) -> bool:
    """
    Checks whether an iterable argument is of dimension 1.

    Parameters
    ----------
    x:
        The argument to check.

    Returns
    -------
    out: bool.
        True if the argument is valid data for a trace.
    """
    if isinstance(x, np.ndarray):
        return x.size == 1
    elif iterable(x):
        return len(x) == 1

@typecheck
def scalar(x) -> bool:
    """
    Checks whether an argument is of dimension 1.

    IE it is either :
    - an array / iterable of size 1
    - of a scalar type.

    Parameters
    ----------
    x:
        The argument to check.

    Returns
    -------
    out: bool.
        True if the argument is valid data for a trace.
    """
    if iterable(x):
        return _iterable_scalar(x)
    else:
        return True
