# App where:
#  IN money amount
#  In currency
#  Out money amount
in_currency = input("Enter currency: ")    # str < "USD", "EUR"
in_money    = int(input("Enter money: "))  # int < 1000

data_USD_to_EUR_rate = 0.8
data_EUR_to_USD_rate = 1.25

# LOGIC
if in_currency == "USD":
    out_money = in_money * data_USD_to_EUR_rate
    print(out_money, "EUR")
else:
    out_money = in_money * data_EUR_to_USD_rate
    print(out_money, "USD")  
