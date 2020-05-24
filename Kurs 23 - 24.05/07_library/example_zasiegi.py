

# Napisz program z graficznym interfejsem użytkownika (GUI) do obliczania kosztów przejazdu na zadanym dystansie
# dystansie na podstawie spalania samochodu oraz ceny paliwa.
# -> Skorzystaj z modułu tkinter


import tkinter

from tkinter import messagebox

def sumuj():
    try:
        val_a = int(a_entry.get())
        val_b = int(b_entry.get())
        val_c = int(c_entry.get())
        suma = val_a * val_b * val_c / 100
        wynik.configure(text=suma)
    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")

root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Odległość")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="Średnie spalanie")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

c_label = tkinter.Label(master=root, text="Wymagana ilość paliwa")
c_label.pack()
c_entry = tkinter.Entry(master=root)
c_entry.pack()

wynik_labl = tkinter.Label(master=root, text="Wynik:")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()
submit = tkinter.Button(master=root, text="Policz", command=sumuj)
submit.pack()
root.mainloop()
print("Po mainloop")