#! python3
#insecure password manager

password = {'email' :'something', 'blog':'something else', 'bank':'i dont know'}

import pyperclip
import sys
if len(sys.argv) < 2:
	print('usage: python pw.py[account]-copy account password')
	sys.exit()
account = sys.argv[1]     #first command line is the account name
if account in password:
	pyperclip.copy(password[account])
	print('password for'+ account +'copied to the clipboard')
else:
	print('there is no account named'+ account)
