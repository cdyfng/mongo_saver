# -*- coding:utf-8 -*-

"""
> 策略执行的几个步骤:
    1. 取2个市场的盘口价格(okex usdt期货和binance现货)，比较价格超过一定阈值，发出提醒；
    2. **；
 """
import sys
import os

from quant import const
from quant.utils import tools
from quant.utils import logger
from quant.config import config
from quant.market import Market
from quant.trade import Trade
from quant.order import Order
from quant.market import Orderbook, Kline
from quant.data import KLineData
from quant.order import ORDER_ACTION_BUY, ORDER_STATUS_FAILED, ORDER_STATUS_CANCELED, ORDER_STATUS_FILLED


class MyStrategy:

    def __init__(self):
        """ 初始化
        """
        self.strategy = config.strategy
        self.platform = const.OKEX_SWAP
        self.account = config.accounts[0]["account"]
        self.access_key = config.accounts[0]["access_key"]
        self.secret_key = config.accounts[0]["secret_key"]
        self.symbol = config.symbol

        self.kline_data = KLineData(self.platform)

        # 交易模块
        cc = {
            "strategy": self.strategy,
            "platform": self.platform,
            "symbol": self.symbol,
            "account": self.account,
            "access_key": self.access_key,
            "secret_key": self.secret_key,
            "order_update_callback": self.on_event_order_update
        }
        # self.trader = Trade(**cc)

        # 订阅行情
        Market(const.MARKET_TYPE_KLINE, self.platform, self.symbol, self.on_event_kline_update)
        #Market(const.MARKET_TYPE_ORDERBOOK, "okex_swap","BTC-USDT-SWAP", self.on_event_orderbook_update)

    async def on_event_kline_update(self, kline: Kline):
        """ 订单薄更新
        """
        #logger.debug("orderbook:", orderbook, caller=self)
        #save order
        #logger.debug("orderbook.platform:", orderbook.platform, caller=self)
        #logger.debug("orderbook.timestamp:", orderbook.timestamp, caller=self)
        #if orderbook.platform == 'okex_swap': 
        #logger.info('exchange:', orderbook.platform)
        await self.kline_data.create_new_kline(kline)
        logger.info("kline: ", kline)

    async def on_event_order_update(self, order: Order):
        """ 订单状态更新
        """
        logger.info("order update:", order, caller=self)




def main():
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = None

    from quant.quant import quant
    quant.initialize(config_file)
    MyStrategy()
    quant.start()


if __name__ == '__main__':
    main()
