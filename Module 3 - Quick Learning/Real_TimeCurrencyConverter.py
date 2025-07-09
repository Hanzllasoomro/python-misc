from forex_python.converter import CurrencyRates, RatesNotAvailableError
from pprint import pprint  # For clean display of currency rates

def show_all_currencies(rates):
    print("\n🌐 Available Currencies:")
    print("-" * 40)
    for currency in sorted(rates.keys()):
        print(currency, end='  ')
    print("\n" + "-" * 40)

def show_exchange_rates(rates, base='USD'):
    print(f"\n💱 Exchange Rates relative to {base}:")
    print("-" * 40)
    for currency, rate in sorted(rates.items()):
        print(f"{base} → {currency} = {rate:.4f}")
    print("-" * 40)

def main():
    c = CurrencyRates()
    try:
        # Get all currency rates relative to USD
        rates = c.get_rates('USD')

        # Display all currencies and their exchange rates
        show_all_currencies(rates)
        show_exchange_rates(rates)

        # Take user input
        amount = float(input("\n💰 Enter the amount you want to convert: "))
        from_currency = input("🔄 Convert from (currency code): ").upper()
        to_currency = input("➡️ Convert to (currency code): ").upper()

        # Perform conversion
        print(f"\n🔄 Converting {amount} {from_currency} to {to_currency}...")
        result = c.convert(from_currency, to_currency, amount)
        print(f"✅ Converted Amount: {result:.2f} {to_currency}")

    except RatesNotAvailableError:
        print("❌ Currency rates not available. Please check your internet connection or try again later.")
    except ValueError:
        print("❌ Invalid input. Please enter numeric amount and valid currency codes.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
