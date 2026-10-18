import csv


class ExchangeRates:
    def __init__(self, filename):
        self.__filename = filename

        with open(self.__filename, newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        last_row = rows[-1]
        self.__usd_cad = float(last_row["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return amount
        elif from_currency == "USD" and to_currency == "CAD":
            return amount * self.__usd_cad
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.__usd_cad


if __name__ == "__main__":
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD or CAD): ")
    to_currency = input("Convert to (USD or CAD): ")

    result = rates.convert(amount, from_currency, to_currency)

    print("${:,.2f} {} = ${:,.2f} {}".format(
        amount,
        from_currency.upper(),
        result,
        to_currency.upper()
    ))