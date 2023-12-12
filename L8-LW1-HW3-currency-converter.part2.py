# App where:
#  IN money amount
#  In currency
#  Out money amount
in_currency = input("Enter currency: ")    # str < "USD", "EUR"
in_money    = int(input("Enter money: "))  # int < 1000

data_USD_to_EUR_rate = 0.8
data_EUR_to_USD_rate = 1.25
data_MDL_to_EUR_rate = 0.05
data_RUB_to_EUR_rate = 0.01
data_RON_to_EUR_rate = 0.2
data_GBP_to_EUR_rate = 1.17

# LOGIC
match in_currency:
    case "USD":
        out_money = in_money * data_USD_to_EUR_rate
        print(out_money, "EUR")
    case "EUR":
        out_money = in_money * data_EUR_to_USD_rate
        print(out_money, "USD")
    case "MDL":
        out_money = in_money * data_MDL_to_EUR_rate
        print(out_money, "EUR")
    case "RUB":
        out_money = in_money * data_RUB_to_EUR_rate
        print(out_money, "EUR")
    case "RON":
        out_money = in_money * data_RON_to_EUR_rate
        print(out_money, "EUR")
    case "GBP":
        out_money = in_money * data_GBP_to_EUR_rate
        print(out_money, "EUR")
    case _:
        print(f"Sorry! {in_currency} are out of stock.")
