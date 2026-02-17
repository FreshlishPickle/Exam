import os

class stock_info:
    def __init__(self):
        self.symbol = None
        self.first_day = None
        self.first_price = None
        self.last_day = None
        self.last_price = None
        self.count = None
        self.max_price = None
        self.max_price_date = None
        self.min_price = None
        self.min_price_date = None
        self.mean_price = None
        self.range_price = None

    # Datei laden (Pfad!)
    def load_data(self, filepath):
        try:
            dates = []
            prices = []

            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    date, price = line.split()
                    dates.append(date)
                    prices.append(float(price))

            if len(prices) < 2:
                raise ValueError("Nicht genügend Daten")

            self.symbol = os.path.basename(filepath).replace(".csv", "")
            self.first_day = dates[0]
            self.first_price = prices[0]
            self.last_day = dates[-1]
            self.last_price = prices[-1]
            self.count = len(prices)

            self.calc_max(prices, dates)
            self.calc_min(prices, dates)
            self.calc_mean(prices)
            self.calc_range()

        except Exception:
            self.__init__()  # setzt alles wieder auf None

    # Berechnungsmethoden
    def calc_max(self, prices, dates):
        self.max_price = max(prices)
        self.max_price_date = dates[prices.index(self.max_price)]

    def calc_min(self, prices, dates):
        self.min_price = min(prices)
        self.min_price_date = dates[prices.index(self.min_price)]

    def calc_mean(self, prices):
        self.mean_price = sum(prices) / len(prices)

    def calc_range(self):
        if self.max_price is not None and self.min_price is not None:
            self.range_price = self.max_price - self.min_price

    # Getter (wichtig für Teil 2 & 3)
    def get_value(self, value):
        return value if value is not None else "keine Daten verfügbar"


import tkinter as tk
from tkinter import filedialog

def choose_file():
    path = filedialog.askopenfilename(filetypes=[("CSV Dateien", "*.csv")])
    if not path:
        return
    stock.load_data(path)
    update_labels()

def update_labels():
    for key, lbl in labels.items():
        value = stock.get_value(getattr(stock, key))
        lbl.config(text=value)

        if value == "keine Daten verfügbar":
            lbl.config(bg="red", fg="black")
        else:
            lbl.config(bg="white", fg="black")

stock = stock_info()

root = tk.Tk()
root.title("Aktienanalyse")

tk.Button(root, text="CSV-Datei auswählen", command=choose_file)\
    .grid(row=0, column=0, columnspan=2, pady=5)

labels = {}
fields = [
    ("symbol", "Symbol"),
    ("first_day", "Erster Tag"),
    ("first_price", "Preis erster Tag"),
    ("last_day", "Letzter Tag"),
    ("last_price", "Preis letzter Tag"),
    ("count", "Anzahl Preise"),
    ("max_price", "Maximalpreis"),
    ("max_price_date", "Datum Maximalpreis"),
    ("min_price", "Minimalpreis"),
    ("min_price_date", "Datum Minimalpreis"),
    ("mean_price", "Durchschnittspreis"),
    ("range_price", "Spannweite")
]

for i, (attr, text) in enumerate(fields, start=1):
    tk.Label(root, text=text, anchor="w").grid(row=i, column=0, sticky="w")
    lbl = tk.Label(root, text="keine Daten verfügbar",
                   bg="red", fg="black", width=30)
    lbl.grid(row=i, column=1)
    labels[attr] = lbl

root.mainloop()
