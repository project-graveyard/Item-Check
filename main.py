import item_check
import item_list
import item_update
from clear_screen import clear


print('{0:^60}'.format('='*33))
print('{0:^60}'.format('welcome to item check counter').upper())
print('{0:^60}'.format('='*33))


while True:
    print('1. Start Item Check')
    print('2. Check Items Available')
    print('3. Update Stock')
    print('4. Exit\n')
    print("To clear screen, Enter \'clear\'\n")

    data = input('Enter option number: ')
    if data == '1':
        item_check.itemCount()
    elif data == '2':
        item_list.itemChk()
    elif data == '3':
        item_update.index()
    elif data == "clear":
        clear()
    elif data == '4':
        break
    else:
        print('invalid input, try again\n')
        continue
