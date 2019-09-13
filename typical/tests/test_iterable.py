#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np

import pytest
from numpy.testing import assert_allclose

import typical

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
        typical.scalar,
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
        typical.scalar,
        ok_scalar))
