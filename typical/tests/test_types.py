#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np
import sympy as smp

import pytest
from numpy.testing import assert_allclose

import typical as types

#####################################################################
# GENERIC PREDICATES
#####################################################################

def test_anything():
    bullshit = [
        None,
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        tuple,
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4),
        np.inf,
        3,
        -9.45,
        math.pi,
        True,
        np.bool_(64)]

    for x in bullshit:
        assert types.anything(x)

def test_nothing():

    bullshit = [
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        tuple,
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4),
        np.inf,
        3,
        -9.45,
        math.pi,
        True,
        (None, None),
        np.bool_(64)]

    for x in bullshit:
        assert not types.nothing(x)

    assert types.nothing(None)

def test_exactly():
    bullshit = [
        (list, []),
        (lambda x: 3 * x, lambda x: 3 * x), # doesn't work ?
        (True, 67),
        (True, bool),
        (True, bool()),
        (True, (1,)),
        (45, -6),
        (45, lambda x: 45),
        (np.inf, 45),
        (None, 'r'),
        (None, ''),
        (None, list()),
        (types.exactly, types.one_of),
        (types.numeric, types.numeric(4))]

    ok = [
        (list(), []),
        (True, bool(67)),
        (True, bool((1,))),
        (45, 10+35),
        ('truc test', 'truc ' + 'test')]

    for pair in bullshit:
        assert not types.exactly(pair[0])(pair[1])
        assert not types.exactly(pair[1])(pair[0])

    for pair in ok:
        assert types.exactly(pair[0])(pair[1])
        assert types.exactly(pair[1])(pair[0])

def test_one_of():
    x, y, z = smp.symbols('x y z')

    ok_spec = [
        {'a': (-2, 345)},
        {1: (-1, -1), 'z': (9, 9.3)},
        {'test': (3.4, 9.2)}]

    ok_symbolic = [
        3,
        -9.45,
        math.pi,
        np.inf,
        True,
        np.bool_(64),
        x,
        x * y + z,
        smp.cos(y),
        4.5 * z ** x]

    for a in ok_spec:
        assert types.one_of(types.numeric, types.symbolic)(a)
        assert types.one_of(types.finite)(a)
        assert types.one_of(types.symbolic, types.iterable)(a)

    for a in ok_symbolic:
        assert not types.one_of(types.iterable, types.specifications)(a)
        assert types.one_of(types.iterable, types.symbolic)(a)

    assert types.one_of(
        types.exactly('truc'),
        types.finite,
        types.exactly(list()))([])

def test_all_of():
    x, y, z = smp.symbols('x y z')

    ok_spec = [
        {'a': (-2, 345)},
        {1: (-1, -1), 'z': (9, 9.3)},
        {'test': (3.4, 9.2)}]

    ok_symbolic = [
        3,
        -9.45,
        math.pi,
        np.inf,
        True,
        np.bool_(64),
        x,
        x * y + z,
        smp.cos(y),
        4.5 * z ** x]

    for a in ok_spec:
        assert not types.all_of(types.numeric, types.symbolic)(a)
        assert types.all_of(types.finite)(a)
        assert types.all_of(types.specifications, types.iterable)(a)

    for a in ok_symbolic:
        assert types.all_of(types.scalar, types.symbolic)(a)
        assert types.one_of(types.finite, types.symbolic)(a)

    assert types.all_of(
        types.exactly(1.5),
        types.finite)(
            1.5)

    assert types.all_of(
        types.exactly(1.5),
        types.finite)(
            1.5)

def test_iterable():
    bullshit = [
        list,
        lambda x: 3 * x,
        True,
        45,
        np.inf,
        np.bool_(None),
        None,
        types.numeric,
        types.one_of(types.numeric, types.bounds)]

    ok = [
        range(5),
        np.arange(32).reshape(4, -1),
        np.array((6, 3)),
        "iuuhig"]

    for x in bullshit:
        assert not types.iterable(x)

    for x in ok:
        assert types.iterable(x)

#####################################################################
# NUMERIC PREDICATES
#####################################################################

def test_numeric_on_scalars():
    bullshit = [
        None,
        tuple,
        lambda x, y : x - y]

    ok = [
        np.inf,
        3,
        -9.45,
        math.pi,
        True,
        np.bool_(64)]

    for x in bullshit:
        assert not types.numeric(x)

    for x in ok:
        assert types.numeric(x)

def test_numeric_on_iterables():
    bullshit = [
        'kgjdqlsfj',
        {'tr': 'àdfsg', (4, 5): 5.6}]

    ok = [
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        np.arange(12).reshape(3, 4)]

    for x in bullshit:
        assert not types.numeric(x)

    for x in ok:
        assert types.numeric(x)

def test_finite_on_scalars():
    bullshit = [
        None,
        tuple,
        np.inf,
        lambda x, y : x - y]

    ok = [
        3,
        -9.45,
        math.pi,
        True,
        np.bool_(64)]

    for x in bullshit:
        assert not types.finite(x)

    for x in ok:
        assert types.finite(x)

def test_finite_on_iterables():
    bullshit = [
        'kgjdqlsfj',
        {'tr': 'àdfsg', (4, 5): 5.6},
        (-np.inf, 673),
        dict(a=65, g=np.nan),
        (3.1, np.nan)]

    ok = [
        (-84,),
        (),
        (43, -2),
        {},
        np.arange(12).reshape(3, 4)]

    for x in bullshit:
        assert not types.finite(x)

    for x in ok:
        assert types.finite(x)

#####################################################################
# SYMBOLIC PREDICATES
#####################################################################

def test_symbolic():
    x, y, z = smp.symbols('x y z')

    bullshit = [
        None,
        "dsgiojdgf",
        lambda x, y : x - y,
        tuple,
        {'tr': 'àdfsg', (4, 5): 5.6}]

    ok = [
        3,
        np.inf,
        -9.45,
        math.pi,
        True,
        np.bool_(64),
        x,
        x * y + z,
        smp.cos(y),
        4.5 * z ** x,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        np.arange(12).reshape(3, 4),
        (x, x+y)]

    for a in bullshit:
        assert not types.symbolic(a)

    for a in ok:
        assert types.symbolic(a)

#####################################################################
# BOUNDS PREDICATES
#####################################################################

def test_bounds_predicate_on_bullshit():
    bullshit = [
        3.4,
        "dsgiojdgf",
        lambda x, y : x - y,
        (3.1, np.nan),
        (-84,),
        (),
        (43, -2),
        {},
        {'tr': 'àdfsg', (4, 5): 5.6},
        np.arange(12).reshape(3, 4)]

    for x in bullshit:
        assert not types.bounds(x)

def test_bounds_predicate_on_tuples():
    tuples = [
        (-np.inf, 345),
        (-np.inf, np.inf),
        (9.3, 9.3),
        (3.4, 9)]

    for x in tuples:
        assert types.bounds(x)

def test_bounds_predicate_on_dicts():
    dicts = [
        {'a': (-np.inf, 345)},
        {1: (-np.inf, np.inf), 'z': (9.3, 9.3)},
        {'test': (3.4, 9.2)}]

    for x in dicts:
        assert types.bounds(x)

def test_bounds_predicate_on_arrays():
    arrays = [
        np.arange(12).reshape(6, -1)]

    for x in arrays:
        assert types.bounds(x)

#####################################################################
# SPECIFICATIONS PREDICATES
#####################################################################

def test_specifications_predicate_on_bullshit():
    bullshit = [
        3.4,
        "dsgiojdgf",
        lambda x, y : x - y,
        (True, 49.3),
        (3.1, np.nan),
        {'r': (-np.inf, 4.3)},  # format ok ; sould fail because of the infinite bound 
        (-84,),
        (),
        (43, -2),
        {},
        {'tr': 'àdfsg', (4, 5): (4.5, 9)},
        np.arange(12).reshape(3, 4)]

    for x in bullshit:
        assert not types.specifications(x)

def test_specifications_predicate_on_dicts():
    dicts = [
        {'a': (-2, 345)},
        {1: (-1, -1), 'z': (9, 9.3)},
        {'test': (3.4, 9.2)}]

    for x in dicts:
        assert types.specifications(x)

#####################################################################
# TRACE & CHARTS PREDICATES
#####################################################################

def test_trace_data_predicate_on_bullshit():
    bullshit = [
        3.4,
        "dsgiojdgf",
        lambda x, y : x - y,
        (True, 49.3),
        (3.1, np.nan),
        {'r': (-np.inf, 4.3)},
        (-84,),
        (),
        {},
        {'tr': 'àdfsg', (4, 5): (4.5, 9)},
        np.arange(12).reshape(3, 4),
        {'x': list(), 'y': range(1,4), 'name': 'bs'},   # right keys, empty x
        {'y': range(1,4), 'name': 'bs'},                # x missing
        {'x': range(2), 'y': range(1,4), 'name': 'bs'}, # x and y sizes differ
        {'x': range(12,15), 'y': range(1,4)},           # name missing
        {'x': range(3), 'y': 'abc', 'name': ''}]        # y is not numeric data

    for x in bullshit:
        assert not types.trace_data(x)

def test_trace_data_predicate_on_dicts():
    dicts = [
        {'x': [98375.4, len('sdfdfs'), 21], 'y': range(1,4), 'name': 'random data'},
        {'x': [0, 0, 0], 'y': range(1,4), 'name': ''}]

    for x in dicts:
        assert types.trace_data(x)

#####################################################################
# MATRIX & ARRAY PREDICATES
#####################################################################

def test_scalar_predicate_on_bs():
    bs_scalar = [
        range(10),
        dict(a=12, t='dfhgs'),
        'ligu',
        (int, 'fdgdsf'),
        np.arange(20).reshape(1, -1)]

    assert not any(map(
        types.scalar,
        bs_scalar))

def test_scalar_predicate_on_single_element_iterables():
    ok_scalar = [
        range(1),
        dict(t='dfhgs'),    # scalar but not numeric
        'l',                # same here
        tuple,
        None,
        np.arange(1).reshape(1, -1),
        34576.435]

    assert all(map(
        types.scalar,
        ok_scalar))