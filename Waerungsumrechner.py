import tkinter as tk

rates = {
    "EUR": 1.0,
    "USD": 1.1,
    "JPY": 160.0,
    "SEK": 11.2
}

def umrechnen():
    betrag = float(eingabe.get())
    von = von_var.get()
    nach = nach_var.get()
    ergebnis = betrag / rates[von] * rates[nach]
    ausgabe.config(text=f"{ergebnis:.2f} {nach}")

fenster = tk.Tk()
fenster.title("Währungsrechner")

tk.Label(fenster, text="Betrag").pack()
eingabe = tk.Entry(fenster)
eingabe.pack()

tk.Label(fenster, text="Von").pack()
von_var = tk.StringVar(value="EUR")
tk.OptionMenu(fenster, von_var, *rates.keys()).pack()

tk.Label(fenster, text="Nach").pack()
nach_var = tk.StringVar(value="USD")
tk.OptionMenu(fenster, nach_var, *rates.keys()).pack()

tk.Button(fenster, text="Umrechnen", command=umrechnen).pack()

ausgabe = tk.Label(fenster, text="Ergebnis")
ausgabe.pack()

fenster.mainloop()
