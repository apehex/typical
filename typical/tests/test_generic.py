#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np
import sympy as smp

import pytest
from numpy.testing import assert_allclose

import typical

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
        assert typical.anything(x)

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
        assert not typical.nothing(x)

    assert typical.nothing(None)

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
        (typical.exactly, typical.one_of),
        (typical.numeric, typical.numeric(4))]

    ok = [
        (list(), []),
        (True, bool(67)),
        (True, bool((1,))),
        (45, 10+35),
        ('truc test', 'truc ' + 'test')]

    for pair in bullshit:
        assert not typical.exactly(pair[0])(pair[1])
        assert not typical.exactly(pair[1])(pair[0])

    for pair in ok:
        assert typical.exactly(pair[0])(pair[1])
        assert typical.exactly(pair[1])(pair[0])

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
        assert typical.one_of(typical.numeric, typical.symbolic)(a)
        assert typical.one_of(typical.finite)(a)
        assert typical.one_of(typical.symbolic, typical.iterable)(a)

    for a in ok_symbolic:
        assert not typical.one_of(typical.iterable, typical.specifications)(a)
        assert typical.one_of(typical.iterable, typical.symbolic)(a)

    assert typical.one_of(
        typical.exactly('truc'),
        typical.finite,
        typical.exactly(list()))([])

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
        assert not typical.all_of(typical.numeric, typical.symbolic)(a)
        assert typical.all_of(typical.finite)(a)
        assert typical.all_of(typical.specifications, typical.iterable)(a)

    for a in ok_symbolic:
        assert typical.all_of(typical.scalar, typical.symbolic)(a)
        assert typical.one_of(typical.finite, typical.symbolic)(a)

    assert typical.all_of(
        typical.exactly(1.5),
        typical.finite)(
            1.5)

    assert typical.all_of(
        typical.exactly(1.5),
        typical.finite)(
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
        typical.numeric,
        typical.one_of(typical.numeric, typical.bounds)]

    ok = [
        range(5),
        np.arange(32).reshape(4, -1),
        np.array((6, 3)),
        "iuuhig"]

    for x in bullshit:
        assert not typical.iterable(x)

    for x in ok:
        assert typical.iterable(x)
