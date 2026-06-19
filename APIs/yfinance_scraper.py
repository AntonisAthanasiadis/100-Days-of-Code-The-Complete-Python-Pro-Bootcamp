import yfinance as yf

def get_stock_price(ticker_symbol):
    try:
        # Create a ticker object
        ticker = yf.Ticker(ticker_symbol)

        # Fast quote lookup (includes current price, previous close, volume, etc.)
        info = ticker.fast_info

        print(f"You asked for: {ticker_symbol.upper()} Stock Data")
        print(f"Current Price: ${info['last_price']:.2f}")
        print(f"Previous Close: ${info['previous_close']:.2f}")
        print(f"Day's High:    ${info['day_high']:.2f}")
        print(f"Day's Low:     ${info['day_low']:.2f}")

    except Exception as e:
        print(f"Could not fetch data for {ticker_symbol}: {e}")


# Test with Microsoft
get_stock_price("MSFT")