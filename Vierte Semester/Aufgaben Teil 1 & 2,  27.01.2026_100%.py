import os
from typing import List, Tuple, Optional

class stock_info:
    def __init__(self):
        # Alle Attribute (Default: None)
        self.symbol: Optional[str] = None
        self.first_day: Optional[str] = None
        self.first_price: Optional[float] = None
        self.last_day: Optional[str] = None
        self.last_price: Optional[float] = None
        self.count: Optional[int] = None
        self.max_price: Optional[float] = None
        self.max_price_date: Optional[str] = None
        self.min_price: Optional[float] = None
        self.min_price_date: Optional[str] = None
        self.mean_price: Optional[float] = None
        self.range_price: Optional[float] = None

    # -------- Helper für Getter --------
    def _na(self, value):
        return value if value is not None else "keine Daten verfügbar"

    # -------- Setter (Teil 2) --------
    def setSymbol(self, filepath: str):
        self.symbol = os.path.basename(filepath).replace(".csv", "")

    def setFirstDay(self, dates: List[str]):
        self.first_day = dates[0] if dates else None

    def setFirstPrice(self, prices: List[float]):
        self.first_price = prices[0] if prices else None

    def setLastDay(self, dates: List[str]):
        self.last_day = dates[-1] if dates else None

    def setLastPrice(self, prices: List[float]):
        self.last_price = prices[-1] if prices else None

    def setCount(self, prices: List[float]):
        self.count = len(prices) if prices is not None else None

    # -------- Berechnungs-Methoden (Teil 2) --------
    def calcMaxPrice(self, prices: List[float], dates: List[str]):
        if not prices:
            self.max_price = None
            self.max_price_date = None
            return
        self.max_price = max(prices)
        self.max_price_date = dates[prices.index(self.max_price)] if dates else None

    def calcMinPrice(self, prices: List[float], dates: List[str]):
        if not prices:
            self.min_price = None
            self.min_price_date = None
            return
        self.min_price = min(prices)
        self.min_price_date = dates[prices.index(self.min_price)] if dates else None

    def calcMeanPrice(self, prices: List[float]):
        if not prices:
            self.mean_price = None
            return
        self.mean_price = sum(prices) / len(prices)

    def calcRange(self):
        if self.max_price is None or self.min_price is None:
            self.range_price = None
            return
        self.range_price = self.max_price - self.min_price

    # -------- Getter (Teil 2 & 3) --------
    def getSymbol(self):
        return self._na(self.symbol)

    def getFirstDay(self):
        return self._na(self.first_day)

    def getFirstPrice(self):
        return self._na(self.first_price)

    def getLastDay(self):
        return self._na(self.last_day)

    def getLastPrice(self):
        return self._na(self.last_price)

    def getCount(self):
        return self._na(self.count)

    def getMaxPrice(self):
        return self._na(self.max_price)

    def getMaxPriceDate(self):
        return self._na(self.max_price_date)

    def getMinPrice(self):
        return self._na(self.min_price)

    def getMinPriceDate(self):
        return self._na(self.min_price_date)

    def getMeanPrice(self):
        return self._na(self.mean_price)

    def getRange(self):
        return self._na(self.range_price)

    # -------- Datei laden --------
    def load_data(self, filepath: str):
        """Lädt eine CSV-Datei (jede Zeile: <YYYY-MM-DD> <Preis>) und füllt die Attribute
        über Setter- & Berechnungsmethoden. Bei Fehlern: alles zurück auf None.
        """
        try:
            dates: List[str] = []
            prices: List[float] = []

            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    if len(parts) < 2:
                        continue  # unvollständige Zeilen überspringen
                    date, price = parts[0], parts[1]
                    dates.append(date)
                    prices.append(float(price))

            if len(prices) < 2:
                raise ValueError("Nicht genügend Daten in der Datei.")

            # Setter (erst nach Erstellung Werte setzen)
            self.setSymbol(filepath)
            self.setFirstDay(dates)
            self.setFirstPrice(prices)
            self.setLastDay(dates)
            self.setLastPrice(prices)
            self.setCount(prices)

            # Berechnungen
            self.calcMaxPrice(prices, dates)
            self.calcMinPrice(prices, dates)
            self.calcMeanPrice(prices)
            self.calcRange()

        except Exception:
            # Setzt alles wieder auf None
            self.__init__()


if __name__ == "__main__":
    # filedialog ohne eigenes großes GUI-Fenster
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    # Erst versuchen: eine Datei auswählen (wie in der Aufgabe)
    filepath = filedialog.askopenfilename(
        title="CSV-Datei auswählen",
        filetypes=[("CSV Dateien", "*.csv")]
    )

    stocks = []

    if filepath:
        s = stock_info()
        s.load_data(filepath)
        stocks.append(s)
    else:
        # Optional: Falls User lieber einen Ordner auswählen will (praktisch für viele CSVs)
        folder = filedialog.askdirectory(title="Optional: Ordner mit CSV-Dateien auswählen")
        if folder:
            for filename in os.listdir(folder):
                if filename.lower().endswith(".csv"):
                    s = stock_info()
                    s.load_data(os.path.join(folder, filename))
                    # nur hinzufügen, wenn wirklich Daten geladen wurden
                    if s.symbol is not None:
                        stocks.append(s)

    if not stocks:
        print("Keine Datei ausgewählt oder keine gültigen Daten gefunden.")
    else:
        print("Anzahl geladener Aktien:", len(stocks))
        for aktie in stocks:
            print("----")
            print("Symbol:", aktie.getSymbol())
            print("Erster Tag:", aktie.getFirstDay())
            print("Preis erster Tag:", aktie.getFirstPrice())
            print("Letzter Tag:", aktie.getLastDay())
            print("Preis letzter Tag:", aktie.getLastPrice())
            print("Anzahl Preise:", aktie.getCount())
            print("Maximalpreis:", aktie.getMaxPrice())
            print("Datum Maximalpreis:", aktie.getMaxPriceDate())
            print("Minimalpreis:", aktie.getMinPrice())
            print("Datum Minimalpreis:", aktie.getMinPriceDate())
            print("Durchschnittspreis:", aktie.getMeanPrice())
            print("Spannweite:", aktie.getRange())
