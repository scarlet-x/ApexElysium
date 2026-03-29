import matplotlib.pyplot as plt

def generate_chart(df, supports, resistances, symbol, timeframe):
    plt.figure(figsize=(10,5))

    plt.plot(df['close'], label='Price')

    # Draw support
    for s in supports:
        plt.axhline(y=s)

    # Draw resistance
    for r in resistances:
        plt.axhline(y=r)

    plt.title(f"{symbol} ({timeframe})")
    plt.legend()

    file_path = f"{symbol.replace('/','_')}_{timeframe}.png"
    plt.savefig(file_path)
    plt.close()

    return file_path
