

def decrement(n):
    if n == 0:
        print(0)
    print(n)
    decrement(n-1)

decrement(10)