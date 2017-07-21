# -*- coding: utf-8 -*-
import click
from .tradecalc import (
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
@click.argument("stop", type=float)
@click.argument("insert", type=float)
@click.option("--relative-stop", is_flag=True)
def buy(price, stop, insert, relative_stop):
    """Calc max position for a buy order."""
    sl_price = get_stop_loss_price(price, stop, relative_stop)

    # Max units we can buy
    position_size = get_position_size(insert, get_risk_per_unit(price, sl_price))
    position_value = get_position_value(price, position_size)

    # If you set the SL at `sl_price` you can by for `position_value`
    # at `price` with a maximum loss of `insert`.
    click.echo("Stop Loss at price at {}$".format(sl_price))
    click.echo("Size of position {} units ({}$)".format(position_size, position_value))


@click.command()
@click.argument("price", type=float)
@click.argument("stop", type=float)
@click.argument("insert", type=float)
@click.option("--relative-stop", is_flag=True)
def sell(price, stop, insert, relative_stop):
    """Calc max position for a sell order."""
    sl_price = get_stop_loss_price(price, stop * -1, relative_stop)

    # Max units we can buy
    position_size = get_position_size(insert, get_risk_per_unit(price, sl_price))
    position_value = get_position_value(price, position_size)

    # If you set the SL at `sl_price` you can by for `position_value`
    # at `price` with a maximum loss of `insert`.
    click.echo("Stop Loss at price at {}$".format(sl_price))
    click.echo("Size of position {} units ({}$)".format(position_size, position_value))


main.add_command(buy)
main.add_command(sell)
