# RSI

The Relative Strength Index (RSI) is a momentum indicator used in technical analysis to measure how quickly and strongly a price is moving.

It ranges from 0 to 100 and helps identify whether an asset is:
Overbought (price may fall soon)
Oversold (price may rise soon)


RSI increases when recent gains are stronger than losses
RSI decreases when recent losses dominate

At its core, RSI compares average gains vs average losses over a fixed period (typically 14 days):

## RSI Formula

The Relative Strength Index (RSI) is calculated as:

RSI = 100 - 100/(1 + RS)

Where:

RS = Average Gain/Average Loss
	​

## Interpretation
RSI > 70–80 → Overbought (possible downward reversal);
RSI < 30–20 → Oversold (possible upward reversal);
RSI ≈ 50 → Neutral momentum


How the trade signal is generated in the strategy:

The strategy does not directly trade overbought/oversold levels.
Instead, it uses a crossover between RSI and its EMA.

Step 1: Smooth RSI
Compute RSI (14-period)
Compute a 7-period EMA of RSI
This acts like a “signal line” (similar to MACD logic)

Step 2: Generate signals using crossover
Buy (Go Long)
When RSI crosses above its EMA
Momentum is strengthening upward
Sell (Go Short)
When RSI crosses below its EMA
Momentum is turning downward


## Intuition behind the strategy

Think of it like this:
RSI = raw momentum;
EMA of RSI = smoothed momentum trend

So;
RSI crossing above EMA → momentum is accelerating upward → bullish signal
RSI crossing below EMA → momentum is weakening → bearish signal

Position behavior:

The strategy is always in the market
It flips position on every signal:
Long → Short when bearish crossover happens
Short → Long when bullish crossover happens
