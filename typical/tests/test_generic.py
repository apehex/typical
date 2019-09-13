#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np
import sympy as smp

import pytest
from numpy.testing import assert_allclose

from typical.generic import (
    anything,
    all_of,
    exactly,
    nothing,
    one_of,
    iterable)
from typical.iterable import scalar
from typical.numeric import finite, numeric
from typical.optimization import bounds, specifications
from typical.symbolic import symbolic

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
        assert anything(x)

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
        assert not nothing(x)

    assert nothing(None)

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
        (exactly, one_of),
        (numeric, numeric(4))]

    ok = [
        (list(), []),
        (True, bool(67)),
        (True, bool((1,))),
        (45, 10+35),
        ('truc test', 'truc ' + 'test')]

    for pair in bullshit:
        assert not exactly(pair[0])(pair[1])
        assert not exactly(pair[1])(pair[0])

    for pair in ok:
        assert exactly(pair[0])(pair[1])
        assert exactly(pair[1])(pair[0])

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
        assert one_of(numeric, symbolic)(a)
        assert one_of(finite)(a)
        assert one_of(symbolic, iterable)(a)

    for a in ok_symbolic:
        assert not one_of(iterable, specifications)(a)
        assert one_of(iterable, symbolic)(a)

    assert one_of(
        exactly('truc'),
        finite,
        exactly(list()))([])

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
        assert not all_of(numeric, symbolic)(a)
        assert all_of(finite)(a)
        assert all_of(specifications, iterable)(a)

    for a in ok_symbolic:
        assert all_of(scalar, symbolic)(a)
        assert one_of(finite, symbolic)(a)

    assert all_of(
        exactly(1.5),
        finite)(
            1.5)

    assert all_of(
        exactly(1.5),
        finite)(
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
        numeric,
        one_of(numeric, bounds)]

    ok = [
        range(5),
        np.arange(32).reshape(4, -1),
        np.array((6, 3)),
        "iuuhig"]

    for x in bullshit:
        assert not iterable(x)

    for x in ok:
        assert iterable(x)
