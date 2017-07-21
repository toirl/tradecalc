# -*- coding: utf-8 -*-
import click
from tradecalc.tradecalc import (
    get_stop_loss_price,
    get_risk_per_unit,
    get_position_size,
    get_position_value
)


@click.group()
def main(args=None):
    """Console script for tradingtool"""


@click.command()
@click.argument("price", type=float)
@click.argument("risk", type=float)
@click.argument("insert", type=float)
@click.option("--absolut-risk", is_flag=True)
def buy(price, risk, insert, absolut_risk):
    """Show the max size (and volume) of a position you can buy at a given
    `price` with the calculated `risk` to loose your `insert`. The
    position size is calculated by the current `price` and the `risk`
    you want to backup (raising, falling prices) with a maximum loss of
    `insert`. The risk is given in percent on default but may also be
    provided as absolut values.
    """
    sl_price = get_stop_loss_price(price, risk, absolut_risk)

    # Max units we can buy
    position_size = get_position_size(insert, get_risk_per_unit(price, sl_price))
    position_value = get_position_value(price, position_size)

    # If you set the SL at `sl_price` you can by for `position_value`
    # at `price` with a maximum loss of `insert`.
    click.echo("Stop Loss at price at {}$".format(sl_price))
    click.echo("Size of position {} units ({}$)".format(position_size, position_value))


@click.command()
@click.argument("price", type=float)
@click.argument("risk", type=float)
@click.argument("insert", type=float)
@click.option("--absolut-risk", is_flag=True)
def sell(price, risk, insert, absolut_risk):
    """Show the max size (and volume) of a position you can sell at a given
    `price` with the calculated `risk` to loose your `insert`. The
    position size is calculated by the current `price` and the `risk`
    you want to backup (raising, falling prices) with a maximum loss of
    `insert`. The risk is given in percent on default but may also be
    provided as absolut values.
    """
    sl_price = get_stop_loss_price(price, risk * -1, absolut_risk)

    # Max units we can buy
    position_size = get_position_size(insert, get_risk_per_unit(price, sl_price))
    position_value = get_position_value(price, position_size)

    # If you set the SL at `sl_price` you can by for `position_value`
    # at `price` with a maximum loss of `insert`.
    click.echo("Stop Loss at price at {}$".format(sl_price))
    click.echo("Size of position {} units ({}$)".format(position_size, position_value))


main.add_command(buy)
main.add_command(sell)
