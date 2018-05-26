birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}



while True:
    print("enter a name:")
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + 'is the birthday of' + name)
    else:
        print('i dont have any info for that' + name)
        print('what is their birthday?')
        birthdays[name] = input()
        print('birthday database updated')