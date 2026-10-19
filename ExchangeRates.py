import csv

# Exchange rate calculator for USD and CAD
class ExchangeRates:
    def __init__(self, filename):
        self.__filename = filename

        # Read exchange rate data from the CSV file
        with open(self.__filename, newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # The final row contains the latest USD/CAD exchange rate
        last_row = rows[-1]
        self.__usd_cad = float(last_row["FXAUSDCAD"])

    # Convert an amount between USD and CAD
    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return amount
        elif from_currency == "USD" and to_currency == "CAD":
            return amount * self.__usd_cad
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.__usd_cad


# Create an ExchangeRates object using the Bank of Canada data file
if __name__ == "__main__":
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

 # Collect conversion information from the user
    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD or CAD): ")
    to_currency = input("Convert to (USD or CAD): ")

    result = rates.convert(amount, from_currency, to_currency)

# Display the result of the conversion
    print("${:,.2f} {} = ${:,.2f} {}".format(
        amount,
        from_currency.upper(),
        result,
        to_currency.upper()
    ))