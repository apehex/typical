#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np

import pytest
from numpy.testing import assert_allclose

from typical.numeric import finite, numeric

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
        assert not numeric(x)

    for x in ok:
        assert numeric(x)

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
        assert not numeric(x)

    for x in ok:
        assert numeric(x)

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
        assert not finite(x)

    for x in ok:
        assert finite(x)

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
        assert not finite(x)

    for x in ok:
        assert finite(x)
