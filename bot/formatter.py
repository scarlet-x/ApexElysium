def format_output(symbol, tf, supports, resistances):
    return f"""
📊 {symbol} ({tf})

Support:
{', '.join([str(round(s,2)) for s in supports])}

Resistance:
{', '.join([str(round(r,2)) for r in resistances])}
"""
