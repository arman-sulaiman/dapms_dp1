def letter_and_point(percent: float):
    if percent >= 95: return "A+", 4.00
    if 85 <= percent <= 94: return "A", 4.00
    if 80 <= percent <= 84: return "A-", 3.80
    if 75 <= percent <= 79: return "B+", 3.30
    if 70 <= percent <= 74: return "B", 3.00
    if 65 <= percent <= 69: return "B-", 2.80
    if 60 <= percent <= 64: return "C+", 2.50
    if 55 <= percent <= 59: return "C", 2.20
    if 50 <= percent <= 54: return "D", 1.50
    return "F", 0.00
