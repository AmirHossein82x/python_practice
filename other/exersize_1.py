a = [1, 2, 3, 4, 5]
b = list(map(lambda x: x **3 if x == 2 else 0, a))
print("bravo" if all(b) else "bravo bravo")
