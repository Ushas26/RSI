import backtrader as bt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as pt


# 1. Download BTC-USD Data

data = yf.download("BTC-USD", start="2018-01-01", end="2024-01-01")



if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Keep only required columns
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.dropna(inplace=True)


# 2. Define Strategy

class RSICrossoverStrategy(bt.Strategy):
    params = (
        ('rsi_period', 14),
        ('ema_period', 7),
    )

    def __init__(self):
        # RSI indicator
        self.rsi = bt.indicators.RSI(self.data.close, period=self.params.rsi_period)

        # EMA of RSI
        self.rsi_ema = bt.indicators.EMA(self.rsi, period=self.params.ema_period)

        # Crossover signal
        self.crossover = bt.indicators.CrossOver(self.rsi, self.rsi_ema)

    def next(self):
        # If not in position
        if not self.position:
            if self.crossover > 0:
                self.buy()  # Long
            elif self.crossover < 0:
                self.sell()  # Short

        # If already in position
        else:
            if self.crossover > 0:
                self.close()
                self.buy()
            elif self.crossover < 0:
                self.close()
                self.sell()



# 3. Set up Cerebro Engine

cerebro = bt.Cerebro()

# Add strategy
cerebro.addstrategy(RSICrossoverStrategy)

# Convert pandas data to backtrader feed
data_feed = bt.feeds.PandasData(dataname=data)
cerebro.adddata(data_feed)

# Set initial cash
cerebro.broker.setcash(10000)

# Set commission (e.g. 0.1%)
cerebro.broker.setcommission(commission=0.001)

# Position sizing (fixed size)
cerebro.addsizer(bt.sizers.FixedSize, stake=1)


# 4. Run Backtest

print(f"Starting Portfolio Value: {cerebro.broker.getvalue():.2f}")

cerebro.run()

print(f"Final Portfolio Value: {cerebro.broker.getvalue():.2f}")

cerebro.plot(style='candlestick')