import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Currency():
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = ''.join(i for i in currency_code if not i.isalnum() or i.isspace)

    def __eq__(self, other):
        return self.currency_code == other.currency_code and self.amount == other.amount

    # def __str__(self):
    #     return self.

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount + other.amount
        else:
            raise DifferentCurrencyCodeError()

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount - other.amount
        else:
            raise DifferentCurrencyCodeError()

    def __mul__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount * other.amount, self.currency_code).amount
        else:
            raise DifferentCurrencyCodeError()


class DifferentCurrencyCodeError(Exception):
    pass


class CurrencyConverter():
    def __init__(self, conversion_dict):
        self.conversion_dict = conversion_dict

    def convert_currency(conversion_dict, code_one, code_two):
        self.new_rate = conversion_dict[code_one] * conversion_dict[code_two]
        return new_rate



def main():
    conversion_dict = {
    'USD':1.0,
    'EUR':0.74,
    'YEN': 0.49
    }

    cc = CurrencyConverter(conversion_dict)

currency_one = Currency(5.5, 'USD')
currency_two = Currency(5.5, 'USD')
currency_three = Currency(5, 'JPN')

# print("multiply same is type:", type(result))
print("multiply same is :", currency_one * currency_two)
print("multiply same float is :", currency_one * currency_two)


print("added ", currency_one + currency_two)
# print("added with different code", currency_one + currency_three)
print("sub ", currency_one - currency_two)
# print("sub with different code", currency_one - currency_three)
print('equal', currency_one == currency_two)
print('not equal', currency_one != currency_three)

if __name__ == '__main__':
    main()
