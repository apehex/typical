# -*- coding: utf-8 -*-

"""
====================
Plottable Predicates
====================
"""

from __future__ import division, print_function, absolute_import

from .generic import iterable
from .numeric import finite
from .typical import checks

#####################################################################
# TRACE & CHARTS PREDICATES
#####################################################################

@checks
def trace_data(x) -> bool:
    """
    Checks whether an argument contains graphing data.

    Parameters
    ----------
    x:
        The argument to check.

    Returns
    -------
    out: bool.
        True if the argument is valid data for a trace.
    """
    return (
        isinstance(x, dict)
        and (
            'x' in x.keys()
            and iterable(x.get('x'))
            and bool(x.get('x'))
            and all(map(finite, x.get('x'))))
        and (
            'y' in x.keys()
            and iterable(x.get('y'))
            and bool(x.get('y'))
            and all(map(finite, x.get('y'))))
        and len(x.get('x')) == len(x.get('y'))
        and 'name' in x.keys())
