def find_levels(df):
    supports = []
    resistances = []

    for i in range(2, len(df)-2):

        if df['low'][i] < df['low'][i-1] and df['low'][i] < df['low'][i+1]:
            supports.append(df['low'][i])

        if df['high'][i] > df['high'][i-1] and df['high'][i] > df['high'][i+1]:
            resistances.append(df['high'][i])

    return supports[-3:], resistances[-3:]
