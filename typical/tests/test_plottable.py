#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests the type checking predicates."""

import math
import numpy as np

import pytest
from numpy.testing import assert_allclose

import typical

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
        assert not typical.trace_data(x)

def test_trace_data_predicate_on_dicts():
    dicts = [
        {'x': [98375.4, len('sdfdfs'), 21], 'y': range(1,4), 'name': 'random data'},
        {'x': [0, 0, 0], 'y': range(1,4), 'name': ''}]

    for x in dicts:
        assert typical.trace_data(x)
