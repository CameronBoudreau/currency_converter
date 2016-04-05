from currency import *

class CurrencyConverter():
    def __init__(self, conversion_dict):
        self.conversion_dict = conversion_dict

### FIX THIS ###
    def convert(self, conversion_dict, currency_one, currency_two, amount):
        converted_amount = amount * self.conversion_dict[currency_one.pass_code()] * self.conversion_dict[currency_two.pass_code()]

        return converted_amount



def main():
    conversion_dict = {
    'USD': 1.0,
    'EUR': 0.74,
    'JPN': 149
    }

    amount = 10

    currency_USD = Currency('USD', amount)
    currency_EUR = Currency('EUR', amount)
    currency_JPY = Currency('JPN', amount)

    converter = CurrencyConverter(conversion_dict)

    converted_amount = converter.convert(conversion_dict, currency_EUR, currency_JPY, amount)
    print("converted amount : ", converted_amount)

    # print(CurrencyConverter.convert(conversion_dict, currency_USD, 10, currency_EUR))

    # test = Currency("$7.50")
    # print(test.symbol_to_code('$7.50'))
    # result = currency_one * currency_two

    # print("multiply same is type:", type(result))
    # print("multiply same is :", currency_one * currency_two)
    # print("multiply same float is :", currency_one * currency_two)
    # print("multiply object type: ", type(currency_one * currency_two))
    #
    # print("added ", currency_one + currency_two)
    # # print("added with different code", currency_one + currency_three)
    # print("sub ", currency_one - currency_two)
    # # print("sub with different code", currency_one - currency_three)
    # print('equal', currency_one == currency_two)
    # print('not equal', currency_USD != currency_EUR)

if __name__ == '__main__':
    main()
