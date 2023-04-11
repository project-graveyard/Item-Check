from item_update import items
import Now


def itemCount():
    itm = []
    prc = []
    qty = []
    atm = []
    amt = 0
    print('\n\n')
    print(' !. Note: If no items are left for input, Enter \'done\'\n')
    while True:
        buy = input('Item bought: ').lower()

        if buy == 'done':
            break
        elif buy not in items.keys():
            print("Not in stock!")
            continue

        qua = input('Quantity of {0}: '.format(buy))

        try:
            int(qua)
        except:
            print('ValueError: Must be an integer')
            continue
        else:
            quant = int(qua)

        itm.append(buy)
        price = items[buy]
        prc.append(price)
        qty.append(quant)
        atm.append(quant * price)
        amt += amt + (quant * price)

    print('\nThe bill is {0}'.format(amt))
    paid = float(input('How much was paid: '))
    bal = paid - amt
    print('\nBalance is: {}'.format(bal))

    # output summary to screen
    print('\n\n\n\n\n')
    Now.timestamp()
    print('\n')
    print("{0:^60}".format('SUMMARY'))
    print('_'*60)
    print("{0:^15}{1:^15}{2:^15}{3:^15}".format(
        'Items', 'Unit Price', 'Quantity', 'Amount'))
    print('_'*60)

    for x in range(len(itm)):
        print("{0:^15}{1:^15}{2:^15}{3:^15}".format(
            itm[x], prc[x], qty[x], atm[x]))

    print('{0:>60}'.format('_'*60))
    print('{0:>45}{1:^15}'.format('Total Amount', amt))
    print('{0:>60}'.format('_'*60))
    print('\nPaid: {0}\nBalance: {1}'.format(paid, bal))

    print('\n\n')
