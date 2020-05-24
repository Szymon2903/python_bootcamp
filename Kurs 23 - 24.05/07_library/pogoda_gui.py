import crime
from tkinter import massagebox
from pogoda import get_location_id, get_location_weather, report

def przygotuj_raport():
    a_entry.get()

root = tkinter.TK()
a_label = tkinter.Label(master=root, text="Wypisz miasto")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
wynik_labl = tkinter.Label(master=root, text="Dane pogody: ")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()
submit = tkinter.Button(master=root, text=f"Szukaj", command=report)
submit.pack()
root.mainloop()

