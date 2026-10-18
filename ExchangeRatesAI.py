"""
FINE 3300 - Assignment 1, Part 2 (Vibe Coding)
ExchangeRatesAI.py

AI-generated exchange rate calculator.
Model used: Claude Opus 5.5 (Anthropic)

Reads the Bank of Canada annual exchange rate file, takes the latest
USD/CAD rate (last row of the file), and converts an amount between
USD and CAD based on the user's input.
"""

import csv


class ExchangeRates:
    """Loads exchange rate data and converts between USD and CAD."""

    def __init__(self, filename):
        # Store the file name and read the latest USD/CAD rate from it
        self.filename = filename
        self.usd_cad = self._load_latest_rate()

    def _load_latest_rate(self):
        """Return the most recent USD/CAD rate (CAD per 1 USD) from the file."""
        # 'utf-8-sig' removes the hidden BOM character at the start of the file
        with open(self.filename, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))

        # The last row of the file holds the latest exchange rate
        latest = rows[-1]
        return float(latest["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency (USD or CAD) to the other."""
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()

        # Same currency: nothing to convert
        if from_currency == to_currency:
            return amount
        # USD -> CAD: multiply by the CAD-per-USD rate
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_cad
        # CAD -> USD: divide by the CAD-per-USD rate
        if from_currency == "CAD" and to_currency == "USD":
            return amount / self.usd_cad

        raise ValueError("Only USD and CAD are supported.")


def main():
    # Create the converter using the Bank of Canada data file
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    # Prompt the user for the amount and the two currencies
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Convert from (USD or CAD): ").strip().upper()
    to_currency = input("Convert to (USD or CAD): ").strip().upper()

    result = rates.convert(amount, from_currency, to_currency)

    # Formatted output: rounded to the nearest penny, with $ and currency codes
    print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")
    print(f"(Exchange rate used: 1 USD = {rates.usd_cad} CAD)")


if __name__ == "__main__":
    main()