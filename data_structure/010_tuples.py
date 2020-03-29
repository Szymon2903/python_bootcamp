# krotka, tupla
x = ( 1, 2, 3, 10, 14, 18, "ala", "mmm", "2.0")
#     0  1  2   3   4   5    6      7      8
print(x)
print(type(x))
print(dir(x))

print(x.index("ala"))
print(x.index('xxxxx'))

print(len(x))
print(len("Ala"))
print(x.count(12))

print("b" in "Olaf")
print(3 in x)
y = "ala ma kota kot "
print(x[0])
print(x[-3])
print(x[0:6])
print([:6])

print(x[::2])
print(y[::-1])
