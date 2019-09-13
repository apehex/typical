#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np

import pytest
from numpy.testing import assert_allclose

from typical.optimization import bounds, specifications

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
        assert not bounds(x)

def test_bounds_predicate_on_tuples():
    tuples = [
        (-np.inf, 345),
        (-np.inf, np.inf),
        (9.3, 9.3),
        (3.4, 9)]

    for x in tuples:
        assert bounds(x)

def test_bounds_predicate_on_dicts():
    dicts = [
        {'a': (-np.inf, 345)},
        {1: (-np.inf, np.inf), 'z': (9.3, 9.3)},
        {'test': (3.4, 9.2)}]

    for x in dicts:
        assert bounds(x)

def test_bounds_predicate_on_arrays():
    arrays = [
        np.arange(12).reshape(6, -1)]

    for x in arrays:
        assert bounds(x)

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
        assert not specifications(x)

def test_specifications_predicate_on_dicts():
    dicts = [
        {'a': (-2, 345)},
        {1: (-1, -1), 'z': (9, 9.3)},
        {'test': (3.4, 9.2)}]

    for x in dicts:
        assert specifications(x)
