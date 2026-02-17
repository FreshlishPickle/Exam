import os

class stock_info:
    def __init__(self):
        self.base_path = r"C:\Users\hayda\Downloads\Aktienkurse5J"

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

    def load_data(self, filename):
        filepath = os.path.join(self.base_path, filename)

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

            self.symbol = filename.replace(".csv", "")

            self.first_day = dates[0]
            self.first_price = prices[0]
            self.last_day = dates[-1]
            self.last_price = prices[-1]
            self.count = len(prices)

            self.calc_max(prices, dates)
            self.calc_min(prices, dates)
            self.calc_mean(prices)
            self.calc_range()

        except Exception as e:
            print(f"Fehler bei {filename}:", e)

    @classmethod
    def load_all_from_folder(cls, folder_path):
        stocks = []

        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".csv"):
                stock = cls()
                stock.base_path = folder_path
                stock.load_data(filename)
                stocks.append(stock)

        return stocks

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

    def get_value(self, value):
        return value if value is not None else "keine Daten verfügbar"


folder = r"C:\Users\hayda\Downloads\Aktienkurse5J"

alle_aktien = stock_info.load_all_from_folder(folder)

print("Anzahl geladener Aktien:", len(alle_aktien))

for aktie in alle_aktien:
    print(
        aktie.symbol,
        aktie.mean_price,
        aktie.max_price,
        aktie.min_price
     )
