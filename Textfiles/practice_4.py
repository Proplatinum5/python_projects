def discount(price: int, discount_total: float) -> float:
    adj_discount = discount_total/100
    print(adj_discount)
    new_total = price*adj_discount
    return new_total

print(discount(100, 50))
