import pandas as pd

def buy_sell_simulation(data, buy_level, sell_level, min_hold_days):
    """
    Generate signals indicating holding status: long (1), or none (0).

    :param data: Pandas DataFrame with 'DATE' as index and price columns.
    :param buy_level: Price level to trigger a buy (enter a long position).
    :param sell_level: Price level to trigger a sell (exit a long position).
    :param min_hold_days: Minimum number of days to hold before selling.
    :return: DataFrame with holding status signals for each column.
    """
    signals = pd.DataFrame(0, index=data.index, columns=data.columns)
    holding_status = {column: False for column in data.columns}
    last_buy_dates = {column: None for column in data.columns}

    for column in data.columns:
        for date, price in data[column].items():  # Using items() for Series
            if holding_status[column] and price >= sell_level:
                if last_buy_dates[column] is None or (date - last_buy_dates[column]).days >= min_hold_days:
                    holding_status[column] = False  # Exit position

            elif not holding_status[column] and price <= buy_level:
                holding_status[column] = True  # Enter position
                last_buy_dates[column] = date

            # Update the signal
            signals.at[date, column] = 1 if holding_status[column] else 0

    return signals

def main(df, buy_level, sell_level, min_hold_days):
    return buy_sell_simulation(df, buy_level, sell_level, min_hold_days)
