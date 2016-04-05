from currency import *

class CurrencyConverter():
    def __init__(self, conversion_dict):
        self.conversion_dict = conversion_dict

    conversion_dict = {
    'USD':1.0,
    'EUR':0.74,
    'YEN': 149
    }

### FIX THIS ###
    def convert(conversion_dict, code_one, amount, code_two):
        print("Value of first dict code: ", conversion_dict[code_one])
        print("Value of first second code: ", conversion_dict[code_two])

        converted_amount = conversion_dict[code_one] * conversion_dict[code_two] * amount
        return converted_amount





conversion_dict = {
'USD':1.0,
'EUR':0.74,
'YEN': 149
}

currency_USD = Currency('USD', 5.5)
currency_EUR = Currency('EUR', 5.34)
currency_JPY = Currency('JPN', 5)


test_converter = CurrencyConverter(conversion_dict)
print(CurrencyConverter.convert(conversion_dict, currency_USD, 10, currency_EUR))
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
print('not equal', currency_USD != currency_EUR)

if __name__ == '__main__':
    main()
