#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tradecalc
----------------------------------

Tests for `tradecalc` module.
"""

from click.testing import CliRunner
from tradecalc import cli


def test_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0


def test_help():
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_buy():
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['buy', '100', '10', '10', '--relative-stop'])
    assert help_result.exit_code == 0
    assert 'Stop Loss at price at 90.0$' in help_result.output


def test_sell():
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['sell', '100', '10', '10', '--relative-stop'])
    assert help_result.exit_code == 0
    assert 'Stop Loss at price at 110.0$' in help_result.output
