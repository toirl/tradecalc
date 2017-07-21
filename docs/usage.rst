=====
Usage
=====
To calculate your maximum position 3 variables must be known:

1. The `buy/sell price` you want to buy/sell some asset.
2. The `stop loss price`. The stop loss price is the price where you close your current position to reduce losses.
3. Your `insert`. You insert is the max amount of money you will set at risk to
   loose in this order.

.. important::

        Following serious risk management you should only insert 1-2% of your total
        credit per trade. This means to do a trade with risk of 100$ to loose you
        should have 100000$ total credit in the back.

        Do not confuse your insert with the value of the trade. Depending on
        your stop loss the total value of your trade will be much higher than
        your insert. See example below.

Calculate position size
-----------------------
Lets say you want to place on order and can risk 100$ to loose in this order.
The current order price is 150$ and you want to set the stop loss at 140$.

To calcule the maximum buy position you can invoke the command like this::

        $ tradecalc buy 150 140 100
        Stop Loss at price at 140.0$
        Size of position 10.0 units (1500.0$)

This means you can buy 10 units of the asset with a total value of 1500$ in
this trade with a risk to loose 100$ in case you set your stop loss at
140$.

To sell a position the command work the same::

        $ tradecalc sell 150 160 100 --absolut-risk
        Stop Loss at price at 160.0$
        Size of position 10.0 units (1500.0$)

This means you can sell 10 units of the asset with a total value of 1500$ in
this trade with a risk to loose 100$ in case you set your stop loss at
160$.
