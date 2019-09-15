# -*- coding: utf-8 -*-

"""
==================
Generic Predicates
==================
"""

from __future__ import division, print_function, absolute_import

from .typical import _check, checks

#####################################################################
# GENERIC PREDICATES
#####################################################################

@checks
def anything(x) -> bool:
    """
    Accepts all the input values.

    Parameters
    ----------
    x :
        An argument to check.

    Returns
    -------
    out: bool.
        Always True.
    """
    return True

@checks
def nothing(x) -> bool:
    """
    Checks whether an input is None.

    Parameters
    ----------
    x :
        An argument to check.

    Returns
    -------
    out: bool.
        True if x is None.
    """
    return x is None

@checks
def exactly(y) -> callable:
    """
    Checks whether an input has exactly the same content as
    a given object y.

    Does not require the compared object to point to the same
    physical address, as long as the content is identical.

    Parameters
    ----------
    y:
        Any object, with the eq operator defined.

    Returns
    -------
    out:
        True if x has the same content as y.
    """
    def _exactly(x):
        return bool(x == y)

    return _exactly

@checks
def one_of(*checkers) -> callable:
    """
    Checks whether an input satisfies at least one of the given checkers.

    Parameters
    ----------
    checkers: list.
        List of checker callables.

    Returns
    -------
    out: bool.
        True of any of the checkers is satisfied.
    """
    def __one_of(x):
        return any([
            _check(x, __checker)
            for __checker in checkers])

    return __one_of

@checks
def all_of(*checkers) -> callable:
    """
    Checks whether an input satisfies all the given checkers.

    Parameters
    ----------
    checkers: list.
        List of checker callables.

    Returns
    -------
    out: bool.
        True of all of the checkers are satisfied.
    """
    def __all_of(x):
        return all([
            _check(x, __checker)
            for __checker in checkers])

    return __all_of

@checks
def iterable(x) -> bool:
    """
    Checks whether an object is iterable.

    Parameters
    ----------
    x:
        The argument to check.

    Returns
    -------
    out: bool.
        True if the argument is iterable.
    """
    try:
        it = iter(x)
    except TypeError:
        return False
    else:
        return True
