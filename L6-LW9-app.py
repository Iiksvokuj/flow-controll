# Solving the situation when the client wants to pay for a service
# - trying to pay by a cach
# - trying to pay by a credit card
# - trying to pay by cryptocurrency

service_price = 100

client_cash_amount = 50
client_card_amount = 50
client_card_crypto = 300


if client_cash_amount >= service_price:
    print('CASH payment success!!!')
else:

    print('CASH payment failure!!!')
    if client_card_amount >= service_price:
        print('CARD payment success!!!')
    else:

        print('CARD payment failure!!!')
        if client_card_crypto >= service_price:
            print('CRYPTO payment success!!!')
        else:
            print('CRYPTO payment failure!!!')