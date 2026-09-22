import decimal
string = "12345"
print(type(string))
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))