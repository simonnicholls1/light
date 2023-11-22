import matplotlib.pyplot as plt
import numpy as np

# Example structure for the 'load' command
def plot(df):
    df.plot()
    title = f"Signal p&l"
    plt.title(title)

    if len(df.columns) == 1:
        # Calculate stats
        md = max_drawdown(df)
        ar = annualized_return(df)
        av = annualized_volatility(df)
        sr = sharpe_ratio(df, ar, av)

        # Prepare text for the stats box
        stats_text = (f"SR: {round(sr,2)}\n"
                      f"Max DD: {round(md*100,2)}%\n"
                      f"Ann Ret: {round(ar*100,2)}%\n"
                      f"Ann Vol: {round(av*100,2)}%")

        # Positioning the text box on the plot
        plt.text(0.70, 0.35, stats_text, transform=plt.gca().transAxes,
                 fontsize=9, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.show()

def annualized_return(df):
    compounded_return = (df.iloc[-1] / df.iloc[0]) - 1
    num_years = len(df) / 252  # Assuming 252 trading days in a year
    ar = (1 + compounded_return) ** (1 / num_years) - 1
    return ar.values[0]

def annualized_volatility(df):
    daily_returns = df.pct_change()
    av = daily_returns.std() * np.sqrt(252)  # Annualizing the standard deviation
    return av.values[0]

def sharpe_ratio(df, ann_return, ann_vol, risk_free_rate=0.0):
    sr = (ann_return - risk_free_rate) / ann_vol
    return sr

def max_drawdown(df):
    rolling_max = df.cummax()
    drawdown = df / rolling_max - 1
    md = drawdown.min()
    return md.values[0]


def main(df):
    plot(df)
    return df