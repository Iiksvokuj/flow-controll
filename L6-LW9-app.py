# Solving the situation when the client wants to pay for a service
# - trying to pay by a cash
# - trying to pay by a credit card
# - trying to pay by cryptocurrency

# HW:
#    - updae the flowchart
#   *- maybe convert crypto to cash / card

service_price = 100  #EUR
data_EUR_to_BTC = 0.0000288
data_BTC_to_EUR = 34700

client_cash_amount = int(input('Enter cash amount, EUR: '))


if client_cash_amount >= service_price:
    print('CASH payment success!!!')
else:

    print('CASH payment failure!!!')
    client_card_amount = int(input('Enter card amount, EUR: '))
    if client_card_amount >= service_price:
        print('CARD payment success!!!')
    else:

        print('CARD payment failure!!!')
        client_card_crypto = int(input('Enter crypto amount, BTC: '))
        client_card_euro = client_card_crypto * data_BTC_to_EUR
        if client_card_euro >= service_price:
            print("Current rate is: 1 BTC = 34700 EUR")
            print("In conversion to EUR you've entered the following amount: ", client_card_euro, "EUR")
            print('CRYPTO payment success!!!')
        else:
            print('CRYPTO payment failure!!!')