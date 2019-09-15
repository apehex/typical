# -*- coding: utf-8 -*-

"""
==================
Checking processes
==================
"""

from __future__ import division, print_function, absolute_import

from decorator import decorator
import inspect

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
def checks(func, *args, **kwargs):
    """
    Function decorator. Checks decorated function is given valid arguments,
    following the information written in the annotations.

    ! NOTE !
    Only checking the varargs ; there's no information to check the kwargs.

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
