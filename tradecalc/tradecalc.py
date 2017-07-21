# -*- coding: utf-8 -*-


def get_stop_loss_price(price, stop, relative_stop=False):
    """Returns the stop loss price. The actual stop loss price is
    calculated from the piven stop. The stop can be set in abosult
    (default) or in relative values to the price.

    Please note that the stop must be positive for BUY orders and
    negative for SELL orders.

    :price: Current price you want to buy/sell.
    :stop: Stop price.
    :relative_stop: Flag that the stop is interpreted as relative value
    and not as absolut value.
    :returns: Price where to set the stop loss
    """
    if relative_stop:
        sl_price = price - stop
    else:
        sl_price = stop
    return sl_price


def get_risk_per_unit(price, sl_price):
    """Returns the risk per unit as difference of the current price
    minus the stop loss price.

    Example:
    If the current price of the unit is 10$ and your stop loss price is
    set to 9$ the risk per unit is 1$

    :price: Current price you want to buy/sell.
    :sl_price: Stop loss pricel.
    :returns: Amount the buy/sell price can raise/fall per unit.
    """
    return abs(price - sl_price)


def get_position_size(insert, risk_per_unit):
    """Returns number of items you can buy with the given insert at the
    given risk.

    Example:
    If you have an max insert to 10$ which you can afford to loose and
    the risk per unit (calculated from the current unit price and its
    stop loss price) is 1$ you can buy 10 units.

    :insert: Max amount of money you set at risk to loose.
    :risk_per_unit: Amount the buy/sell price can raise/fall per unit.
    :returns: Number of units you can buy.
    """
    return insert / risk_per_unit


def get_position_value(price, size):
    """Returns the value of your position. This is the amountof money
    you must set into BUY order or which you get when doing a SELL order.

    :price: Current price you want to buy/sell.
    :size: How many do you want to buy/sell
    :returns: Value of your position.
    """
    return price * size
