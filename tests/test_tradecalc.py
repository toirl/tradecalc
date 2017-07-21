#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tradecalc
----------------------------------

Tests for `tradecalc` module.
"""


def test_get_stop_loss_price():
    from tradecalc.tradecalc import get_stop_loss_price
    # BUY percentage
    sl = get_stop_loss_price(150, 135)
    assert sl == 135
    # SELL percentage
    sl = get_stop_loss_price(150, 165)
    assert sl == 165
    # BUY absolut
    sl = get_stop_loss_price(150, 5, True)
    assert sl == 145
    # SELL absolut
    sl = get_stop_loss_price(150, -5, True)
    assert sl == 155


def test_get_risk_per_unit():
    from tradecalc.tradecalc import get_risk_per_unit
    rpu = get_risk_per_unit(100, 90)
    assert rpu == 10


def test_get_position_size():
    from tradecalc.tradecalc import get_position_size
    ps = get_position_size(100, 5)
    assert ps == 20


def test_get_position_value():
    from tradecalc.tradecalc import get_position_value
    ps = get_position_value(100, 20)
    assert ps == 2000
