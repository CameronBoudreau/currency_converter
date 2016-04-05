class DifferentCurrencyCodeError(Exception):
    pass


class Currency():
    def __init__(self, currency_code, amount= 0):
        self.amount = amount
        self.currency_code = self.symbol_to_code(currency_code)

    symbol_dict = {
    '$':'USD',
    '€':'EUR',
    '¥':'JPY'
    }

    def symbol_to_code(self, currency_code, symbol_dict=symbol_dict):
        if not currency_code.isalnum():
            currency_code = ''.join(i for i in currency_code if not i == '.' and not i.isalnum() or i.isspace())
            return symbol_dict[currency_code]
        else:
            return currency_code.rstrip()

    def __eq__(self, other):
        return self.currency_code == other.currency_code and self.amount == other.amount


    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount + other.amount
        else:
            raise DifferentCurrencyCodeError

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount - other.amount
        else:
            raise DifferentCurrencyCodeError

    def __mul__(self, other):
        return float("%.2f" % Currency(self.amount * other.amount, self.currency_code).amount)
