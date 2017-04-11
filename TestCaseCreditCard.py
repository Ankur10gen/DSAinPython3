from CreditCard import CreditCard

wallet = []
wallet.append(CreditCard('Ankur Raina','CITI','111122223333',100000))
wallet.append(CreditCard('Ravi','AXIS','222333444',100000))
wallet.append(CreditCard('Vivek','KOTAK','555666777',120000))
wallet.append(CreditCard('Manish','UNION','999777888',150000))

for val in range(1,18):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)

for c in range(3):
    print('Customer =', wallet[c].get_customer())
    print('Bank =',wallet[c].get_bank())
    print('Account =',wallet[c].get_account())
    print('Limit =', wallet[c].get_limit())
    print('Balance =',wallet[c].get_liability())
    while wallet[c].get_liability() > 100:
        wallet[c].make_payment(100)
        print('New balance =',wallet[c].get_liability())
    print()
