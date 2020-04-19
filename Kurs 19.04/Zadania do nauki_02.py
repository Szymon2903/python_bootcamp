

# def przywitanie(name="World!"):
#     if name == "xxx":
#         return "Nie używamy brzydkich słów!"
#     return f"Hello {name}"
#
#
# print(przywitanie("Rafał"))
# przywitanie("Adam")
# przywitanie("Marcin")
# przywitanie("Paulina")
# przywitanie("Maria")
# przywitanie("xxx")
# #print(3, x)
# def incrementator(poczatek, krok=1):
#     return poczatek + krok
# print(incrementator(10))  # 11
# print(incrementator(14))  # 15
# print(incrementator(14, 4))  # 18

def zlacz_teksty(lista_textow):
    return " ".join(lista_textow)
lista = ["A", "B", "C"]
print(zlacz_teksty(lista))
t1 = "A"
t2 = "B"
t3 = "C"
def zlacz_teksty(*args, **kwargs):
    #print(args)
    #print(kwargs)
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace(k, str(v))
    return text
slownik = dict(x=10, y=20)
print(slownik)
zlacz_teksty(t1, t2, t3, x=1, y=2, z=10)
zlacz_teksty(t1, t3)
print("-"*40)
print(zlacz_teksty(t1, "xxx", y=10))
print("-"*40)
print(zlacz_teksty(t1, "xxx", x=10))