cat_names = []
while True:
    print('enter the cat name' + str(len(cat_names)+1)+ 'or press enter to end')
    name = input()
    if name == '':
        break
    else:
        cat_names = cat_names + [name]
print('the names are ')
for i in cat_names:
    print(i)




