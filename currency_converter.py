from currency import *

class CurrencyConverter():
    def __init__(self, conversion_dict):
        self.conversion_dict = conversion_dict

### FIX THIS ###
    def convert(self, conversion_dict, currency_one, currency_two, amount):
        converted_amount = Currency(currency_one.currency_code, (float(amount) / self.conversion_dict[currency_one.pass_code()]) * self.conversion_dict[currency_two.pass_code()])

        return converted_amount



def main():
    conversion_dict = {
    'USD': 1.0,
    'EUR': 0.74,
    'JPY': 149
    }


    amount = input("How much would you like to convert?\n> ")
    if amount.isalnum():
        print('Is amount just numbers? ', amount)
        currency_USD = Currency('USD', amount)
        currency_EUR = Currency('EUR', amount)
        currency_JPY = Currency('JPY', amount)
    else:
        print('Does amount have symbols? ', amount)
        currency_USD = Currency(amount)
        currency_EUR = Currency(amount)
        currency_JPY = Currency(amount)

    converter = CurrencyConverter(conversion_dict)

    converted_amount = converter.convert(conversion_dict, currency_USD, currency_JPY, amount)
    print("converted amount : ", converted_amount)


if __name__ == '__main__':
    main()
