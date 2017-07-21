# -*- coding: utf-8 -*-


def get_stop_loss_price(price, risk, absolut_risk=False):
    """Returns the stop loss price. The stop loss price is calculated
    from the current `price` and the risk you want to backup in price
    movement. The risk can be set in percent (default) or in absolut
    values.

    Please note that the risk must be positive for BUY orders and
    negative for SELL orders.

    :price: Current price you want to buy/sell.
    :risk: Risk in sense of of the price raises or falls.
    :absolut_risk: Flag that the risk is interpreted as absolut value
    and not as percentage.
    :returns: Price where to set the stop loss
    """
    if absolut_risk:
        sl_price = price - risk
    else:
        sl_price = price - (price / 100 * risk)
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
