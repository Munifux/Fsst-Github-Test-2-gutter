import tkinter as tk
import random

rates = {
    "EUR": 1.0,
    "USD": 1.1,
    "JPY": 160.0,
    "SEK": 11.2,
    "Döner": 0.15, # Neue Weltwährung hinzugefügt
    "Lotto-Scheine": 0.5
}

def umrechnen():
    # Hintergrundfarbe zufällig ändern (Party-Modus)
    colors = ["red", "yellow", "pink", "green", "cyan", "orange"]
    fenster.config(bg=random.choice(colors))
    
    try:
        betrag_str = eingabe.get()
        
        # Aggressive Fehlermeldung, wenn das Feld leer ist
        if not betrag_str:
            ausgabe.config(text="BIST DU BLIND? GIB NE ZAHL EIN!", fg="red", font=("Arial", 20, "bold"))
            return

        betrag = float(betrag_str)
        
        # 20% Chance, dass das Finanzamt zuschlägt
        if random.random() < 0.20:
            ausgabe.config(text="DAS FINANZAMT HAT ALLES GESTOHLEN! 💸", fg="white", bg="black")
            return

        von = von_var.get()
        nach = nach_var.get()
        
        # Berechnung mit einer kleinen "Zufallsschwankung" (Börsencrash-Simulator)
        chaos_faktor = random.uniform(0.9, 1.1)
        ergebnis = (betrag / rates[von] * rates[nach]) * chaos_faktor
        
        ausgabe.config(text=f"Etwa {ergebnis:.2f} {nach} (vielleicht)", fg="black", bg="white")
        
    except ValueError:
        ausgabe.config(text="Das ist keine Zahl, du Pfannkuchen! 🥞", fg="purple")

fenster = tk.Tk()
fenster.title("SCAM-RECHNER 3000")
fenster.geometry("400x500")

tk.Label(fenster, text="Wieviel Kohle hast du?", font=("Comic Sans MS", 12)).pack(pady=10)
eingabe = tk.Entry(fenster, font=("Arial", 14), justify="center")
eingabe.pack()

tk.Label(fenster, text="Was gibst du her?").pack(pady=5)
von_var = tk.StringVar(value="EUR")
tk.OptionMenu(fenster, von_var, *rates.keys()).pack()

tk.Label(fenster, text="Was willst du dafür?").pack(pady=5)
nach_var = tk.StringVar(value="USD")
tk.OptionMenu(fenster, nach_var, *rates.keys()).pack()

# Der Button bewegt sich theoretisch nicht, aber wir machen ihn riesig
knopf = tk.Button(fenster, text="REICH WERDEN!", command=umrechnen, 
                  bg="gold", font=("Arial", 16, "bold"), height=2)
knopf.pack(pady=20)

ausgabe = tk.Label(fenster, text="Hier steht dein Schicksal", font=("Arial", 12, "italic"))
ausgabe.pack(pady=20)

# Ein kleiner Disclaimer
tk.Label(fenster, text="*Keine Haftung für emotionale Schäden.", font=("Arial", 8)).pack(side="bottom")

fenster.mainloop()
