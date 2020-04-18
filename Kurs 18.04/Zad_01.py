
#Napisz program wypisujący na konsole tabliczke mnożenia dla liczb od 0 do 9 w postaci tabelki


print("   ", end="")
for i in range(10):
    print(f"{1:4}", end="")
print()
print()

for i in range(10):
    print(i, end="   ")
    for j in range(10):

        print(f"{i*j:4}", end="")


    print()
