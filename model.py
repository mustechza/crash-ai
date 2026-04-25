# model.py
def predict(row):
    score = 0

    if row["volatility"] > 2:
        score += 2

    if row["momentum"] > 0:
        score += 1

    if row["low_streak"] >= 3:
        score += 2

    if row["ma5"] > row["ma10"]:
        score += 1

    if score >= 5:
        return "🔥 STRONG SIGNAL"
    elif score >= 3:
        return "⚠️ WEAK SIGNAL"
    return "❌ NO TRADE"
