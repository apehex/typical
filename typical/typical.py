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

from decorator import decorator
import inspect
import numpy as np
import sympy as smp

#####################################################################
# MESSAGES
#####################################################################

def function_arg_types_error(
        fname: str,
        expected: str,
        actual: str,
        flag: int) -> str:
    """
    Convenience function returns nicely formatted error/warning message.

    Parameters
    ----------
    fname: str.
        The name of the function that failed.
    expected: type list.
        The expected type for each parameter.
    actual: type list.
        The types of the given arguments.
    flag: int.
        Whether it was the input or the output that didn't match.

    Returns
    -------
    out: str.
        The error/warning message.
    """
    return "'{}' ".format(fname)\
          + ("accepts ({}), but ", "returns {}, but ")[flag].format(expected)\
          + ("was given", "result is")[flag] + " {}".format(actual)

#####################################################################
# TYPE ENFORCEMENT
#####################################################################

def _check(arg, checker):
    """
    Check a given argument against either a type or a predicate.

    Parameters
    ----------
    arg: anything.
        The argument value.
    checker: type or callable.
        A callable giving a boolean value for any value.

    Returns
    -------
    out: bool.
        Whether the argument satisfies the input constraints.
    """
    if type(checker) == type:
        return isinstance(arg, checker)     #types
    elif callable(checker):
        return checker(arg)                 #predicates
    else:
        return True   

@decorator
def typecheck(func, *args, **kwargs):
    """
    Function decorator. Checks decorated function is given valid arguments,
    following the information written in the annotations.

    ! NOTE !
    Only checking the varargs ; there's no information to chck the kwargs.

    Parameters
    ----------
    func: callable.
        A function on which we want to enforce type checking.

    Returns
    -------
    out: callable.
        The decorated function.
    """
    __result = func(*args, **kwargs)

    if hasattr(func, '__annotations__') and func.__annotations__:
        __arg_spec = inspect.getfullargspec(func)

        for __argname, __arg in zip(__arg_spec.args, args):
            if __argname in func.__annotations__:
                __checker = func.__annotations__[__argname]
                if not _check(__arg, __checker):
                    raise TypeError(function_arg_types_error(
                        func.__name__,
                        "{}:{}".format(__argname, __checker),
                        "{}={}".format(__argname, repr(type(__arg))),
                        0))

        if 'return' in func.__annotations__:
            __checker = func.__annotations__['return']
            if not _check(__result, __checker):
                raise TypeError(function_arg_types_error(
                    func.__name__,
                    "{}".format(__checker),
                    repr(type(__result)),
                    1))

    return __result

#####################################################################
# GENERIC PREDICATES
#####################################################################

@typecheck
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

@typecheck
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

@typecheck
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

@typecheck
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

@typecheck
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

@typecheck
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

#####################################################################
# SYMBOLIC PREDICATES
#####################################################################

@typecheck
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

@typecheck
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

#####################################################################
# TRACE & CHARTS PREDICATES
#####################################################################

@typecheck
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