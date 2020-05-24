

 # Dekotartory

import time

     def milion_kwadratow():
        return len ([x**2 for x in range(1000000)])

     def kwadraty(n):
        return len([x ** 2 for x in range(n)])

     def mierz_czas(func):
         def wrapper(*args, **kwargs):
     start = time.time()
     result = func(*args, **kwargs)
     print(time,time() - start)
     return result

 return wrapper

kwadrat = mierz_czas(milion_kwadratow)

 start = time.time()
 print(milion_kwadratow())
 print(time.time() -start)

 start = time.time()
 print(kwadraty(10000000))
 print(time.time() - start)








class Zwierze:

    def __init__(self, name):
        self.name = name
        self.krolestwo = "Zwierzęta"

    def przedstaw_sie(self):
        print(f"Cześć jestem, {self.name}")
zw = Zwierze("Bugs")
zw.przedstaw_sie()

class Pies(Zwierze):
    def __init__(self, name, rasa):
        super().__init__(name)
        self.rasa = rasa

pies = Pies("Pluto", "Owczarek Podhalański")
pies.przedstaw_sie()
print(pies.rasa)
print(pies.krolestwo)
