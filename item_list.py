from item_update import items

def itemChk():
	print('\n\n')
	print('list of items'.upper())
	print('{0:^30}'.format('_'*30))
	print('{0:^15}{1:^15}'.format('Items', 'Price'))
	print('{0:^30}'.format('_'*30))
	
	for x in items.keys():
		print('{0:^15}{1:^15}'.format(x, items[x]))
	
	print('{0:^30}'.format('_'*30))
	print('\n\n')