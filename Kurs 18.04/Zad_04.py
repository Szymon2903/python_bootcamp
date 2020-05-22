
#Napisz program zliczajacy liczbę wystąpień każdego znaku w podanym przez użytkownika napisie

# 1 PRZYKŁAD

napisz = "ala ma kota"
zliczenia = dict() # {}

for znak in napisz:
    if znak in zliczenia:
        zliczenia[znak] = zliczenia[znak] + 1
    else:
        zliczenia[znak] = 1

for znak in napisz:
    zliczenia[znak] = zliczenia.get(znak, 0) + 1

print(zliczenia)

## 2 PRZYKŁAD

for znak in napisz:
    zliczenia[znak] = napisz.count(znak)
print(zliczenia)

### 3 PRZYKŁAD


for znak in napisz:
    zliczenia[znak] += 1
print( zliczenia)