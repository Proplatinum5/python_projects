def sum_eo(n, t):
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))

cat = int(input(" Enter number"))
print("=" * 30)
dog = input("Enter an e or an o")
print("=" * 30)
x = sum_eo(cat, dog)
print(x)