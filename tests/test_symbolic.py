#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np
import sympy as smp

import pytest
from numpy.testing import assert_allclose

from typical.symbolic import symbolic

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
        assert not symbolic(a)

    for a in ok:
        assert symbolic(a)
