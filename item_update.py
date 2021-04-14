import json

with open("stock.txt", "r") as f:
    items = json.load(f)


def show():
    print('\n\n')
    print('list of items'.upper())
    print('{0:^30}'.format('_'*30))
    print('{0:^15}{1:^15}'.format('Items', 'Price'))
    print('{0:^30}'.format('_'*30))

    for x in items.keys():
        print('{0:^15}{1:^15}'.format(x, items[x]))

    print('{0:^30}'.format('_'*30))


def add():
    print('\n\n')
    print("!. Note: If no items are left for input, Enter \'done\'\n")
    while True:
        new_item = input("Enter new item: ")

        if new_item == "done":
            break
        elif new_item == "":
            print('invalid input, try again\n')
            continue

        new_price = input("Enter unit price of {0}: ".format(new_item))
        print('\n')

        try:
            float(new_price)
        except:
            print("ValueError: Unit price must be a number\nTry again!")
            continue
        else:
            unit_price = float(new_price)

        items[new_item] = unit_price

    with open('stock.txt', 'w') as f:
        json.dump(items, f)
    print('\n\n')
    print("Stocks updated".upper())


def remove():
    print('\n\n')
    print("!. Note: If no items are left for input, Enter \'done\'\n")
    while True:
        item_name = input("Enter the name of item: ")

        if item_name == "done":
            break
        elif item_name == "":
            print('invalid input, try again\n')
            continue

        items.pop(item_name)

    with open('stock.txt', 'w') as f:
        json.dump(items, f)
    print('\n\n')
    print("Stocks updated".upper())


def index():
    while True:
        print('\n\n')
        print("update stocks".upper())
        print('-'*20)
        print("1. Add Item")
        print("2. Remove Item")
        print("3 Exit Stock updates")
        print("!. Enter \'check\' to see stocks list")
        print('\n\n')

        data = input("Enter option: ")
        if data == '1':
            add()
        elif data == '2':
            remove()
        elif data == "check":
            show()
        elif data == '3':
            break
        else:
            print('invalid input, try again\n')
            continue
