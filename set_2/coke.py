def main():
    balance = checkCoin()
    print(f'{balance} Ghana pesewas')


def checkCoin():
    amount = 50
    accpeted_coin = [5, 10, 20]
    amount_inserted = 0
    while amount_inserted <= amount:
        user_coin = int(input('Enter your Coin: '))
        if not user_coin in accpeted_coin:
            continue
        amount_inserted += user_coin
    return amount_inserted - amount


main()
