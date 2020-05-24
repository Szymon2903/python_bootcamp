class Monitor:

  def _init_(self, brand, model):
     self.brand = brand
     self.model = model

  def _str_(self):
     return f"<Monitor {self.brand} | {self.model}>"
     return "<Monitor>"

  def wlacz(self):
      print(self, "włącz sie")

  def wylacz(self):
      print(self, "Wyłączony ...")

lista = list()
lista.append("cos")

m = Monitor("Philips", "M01x1")
m2 = Monitor("Sony", "BV02")
print(m)

m > m2
print(m2)
print(m2.brand)