a = [1 ,5, 6, 7, 8, 9, 10, 12]
a.sort(key=lambda x: x%2 != 0)
print(a)
